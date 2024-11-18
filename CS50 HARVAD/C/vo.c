#include <cs50.h>
#include <string.h>
#include <stdio.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // TODO
    // iteramos sobre todos los nombres para verificar si existe, el nombre que recibimos por el argumento
    // de no recibir un nombre valido, reg¿tornamos false,

    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {

                // Record the preference in the preferences array
                preferences[voter][rank] = i;
                return true;

        }
    }

    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO
    // Iterate through each voter's preferences
    for (int i = 0; i < voter_count; i++)
    {
        // Check each rank for the current voter
        for (int j = 0; j < candidate_count; j++)
        {
            // Get the candidate index from the preferences array
            int candidate_index = preferences[i][j];

            // Check if the candidate is not eliminated
            if (!candidates[candidate_index].eliminated)
            {
                // Increment the candidate's vote count and break out of the loop
                candidates[candidate_index].votes++;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
   // Calculate the minimum number of votes needed to win
    int majority = voter_count / 2 + 1;

    // Iterate through each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the candidate has more than half of the total votes
        if (candidates[i].votes >= majority)
        {
            // Print the winner and return true
            printf("%s\n", candidates[i].name);
            return true;
        }
    }

    // No winner found

    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    // Initialize min_votes to a large value, initially
    int min_votes = MAX_VOTERS + 1;

    // Iterate through each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the candidate is not eliminated and has fewer votes than the current minimum
        if (!candidates[i].eliminated && candidates[i].votes < min_votes)
        {
            // Update the minimum votes
            min_votes = candidates[i].votes;
        }
    }

    // Return the minimum votes
    return min_votes;
    //return 0;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    // Iterate through each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the candidate is not eliminated and has a different number of votes than the minimum
        if (!candidates[i].eliminated && candidates[i].votes != min)
        {
            // If at least one candidate has a different number of votes than the minimum, it's not a tie
            return false;
        }
    }

    // If all remaining candidates have the same number of votes (equal to the minimum), it's a tie
    return true;
    //return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    // Iterate through each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if the candidate has the minimum number of votes
        if (candidates[i].votes == min)
        {
            // Eliminate the candidate by setting the 'eliminated' status to true
            candidates[i].eliminated = true;
        }
    }
    return;
}

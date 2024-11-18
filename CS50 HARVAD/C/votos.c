// Este codigo contiene las variables y algunos comentarios en ingles ya que es
// la complementacion de lo que se plantea en el ejercicio 3 de la semana 3(algoritmos)
// del curso "CS50" de Harvard

#include <cs50.h>
#include <string.h>
#include <stdio.h>

// Maximo de votantes (100)  y maximo de candidatos (9)
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for vote i
// j es la preferencia para el voto en i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
// defenimos una estructura de tipo typedefe, para cada candidato
// tenemos nombre, votos, y una funcion bool la cual nos dice si el candidato
// ya fue eliminado
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
//Definimos un array para candidatos con un valor maximo de 9
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
// definimos 2 variables globales para contar los votos y los candidatos
int voter_count;
int candidate_count;

// prototipos de las funciones
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // verificamos que el usuario agrege al menos un candidato
    if(argc<2)
    {
        printf("Usage: runoff[Candidate...]\n");
        return 1;
    }
    //modificamos el numero de candidatos
    candidate_count=argc-1; 

    // Verificamos que los candidatos sean menos de 9
    if(candidate_count>MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }

    // actualizamos cada espacio en la estructura de candidatos
    for(int i=0;i<candidate_count;i++)
    {
        candidates[i].name=argv[i+1];
        candidates[i].votes=0;
        candidates[i].eliminated=false;
    }

    voter_count=get_int("Numbers of voters: ");
    if(voter_count>MAX_VOTERS)
    {
        printf("Maximum numbers of voters is %i\n",MAX_VOTERS);
        return 3;
    }
    //Sigue consultando por votos
    for(int i=0; i<voter_count;i++)
    {
        // Consulta para cada rango
        for(int j=0;j<candidate_count;j++)
        {
            string name=get_string("Rank %i: ",j+1);

            // Registrar votación, a menos que sea inválida
            if (!vote(i,j,name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }
        printf("\n");
    }

    // Seguir celebrando segundas vueltas hasta que haya un ganador
    while(true)
    {
        // Calcular los votos de los candidatos restantes
        tabulate();
        bool won=print_winner();

        if(won)
        {
            break;
        }

        // Eliminar a los candidatos del último puesto
        int min=find_min();


    }



}

//              i          j          name
bool vote(int voter, int rank, string name)
{
    for(int i=0; i<candidate_count;i++)
    {
        if(strcmp(candidates[i].name,name)==0)
        {
            preferences[voter][rank]=i;
            return true;
        }
    }

}

void tabulate(void)
{
 // Iterar a través de las preferencias de cada votante
    
    for(int i=0;i<voter_count;i++)
    {

       // Compruebe cada rango para el votante actual
        for(int j=0; j<candidate_count;j++)
        {
            // Obtener el índice del candidato de la matriz de preferencias
            int candidate_index=preferences[i][j];
            // Comprobar si el candidato no ha sido eliminado
             if (!candidates[candidate_index].eliminated)
            {
                // Aumentar el número de votos del candidato y salir del bucle
                candidates[candidate_index].votes++;
                break;
            }

        }
    }

}

bool print_winner(void)
{
    // calculamos el minumo de votos para ganar si una segunda vuelta (50%)
    int majority=voter_count/2+1;
    // Iteranos por todos los candidatos

    for(int i=0; i<candidate_count;i++)
    {
        // comprobamos si el candidato tiene mas de la mitad de los votos totales
        if(candidates[i].votes>= majority)
        {
            printf("%s\n",candidates[i].name);
            return true;
        }
    }
    return false;
}

int find_min(void)
{
    // Inicializar min_votes a un valor grande, inicialmente
     int min_votes = MAX_VOTERS + 1;

     for(int i=0;i<candidate_count;i++)
     {
        if(!candidates[i].eliminated && candidates[i].votes<min_votes)
        {
            //actualizamos el minimo de votos
            min_votes=candidates[i].votes;
        }
     }
     return min_votes;

}
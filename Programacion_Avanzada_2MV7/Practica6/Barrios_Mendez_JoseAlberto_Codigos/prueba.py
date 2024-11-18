# Modifying the code to implement the "Simon Says" game logic where each new sequence only adds one new LED
# and retains the previous sequence.

from pyfirmata import Arduino, util
import time
import random

def initialize_board(com_port='COM3'):
    """Initialize connection to Arduino board on the specified COM port."""
    board = Arduino(com_port)
    it = util.Iterator(board)
    it.start()
    return board

def setup_pins(board):
    """Setup button and LED pins."""
    button_pins = [board.get_pin(f'd:{pin}:i') for pin in [9, 10, 11, 12]]
    led_pins = [board.get_pin(f'd:{pin}:o') for pin in [2, 3, 4, 5]]
    return button_pins, led_pins

def wait_for_button_press(button_pins, led_pins):
    """Wait for a button to be pressed and return the index of the pressed button."""
    while True:
        for i, button in enumerate(button_pins):
            if button.read():
                led_pins[i].write(1)  # Turn on LED when button is pressed
                while button.read():  # Wait for button release
                    pass
                led_pins[i].write(0)  # Turn off LED after release
                return i

def add_to_sequence(sequence):
    """Add a new random LED index to the existing sequence."""
    sequence.append(random.randint(0, 3))
    return sequence

def display_sequence(led_pins, sequence):
    """Display a sequence of LEDs."""
    for led_index in sequence:
        led_pins[led_index].write(1)
        time.sleep(0.5)
        led_pins[led_index].write(0)
        time.sleep(0.5)

def receive_responses(button_pins, led_pins, num_responses):
    """Receive a sequence of button responses from the user."""
    responses = []
    for _ in range(num_responses):
        response = wait_for_button_press(button_pins, led_pins)
        responses.append(response)
        print(f"Response received: {response}")
    return responses

def main():
    board = initialize_board()
    button_pins, led_pins = setup_pins(board)
    sequence = []  # Start with an empty sequence
    
    while True:
        sequence = add_to_sequence(sequence)
        print(f"Current sequence: {sequence}")

        display_sequence(led_pins, sequence)
        responses = receive_responses(button_pins, led_pins, len(sequence))

        if sequence == responses:
            print("Correct response, continue.")
        else:
            print("Incorrect response, game over.")
            break
        time.sleep(1)

# Commenting the call to main() to avoid execution
main()

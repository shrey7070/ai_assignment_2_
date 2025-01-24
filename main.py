from functions.state_representation import StateRepresentation
from functions.identify_solution import IdentifySolution
from functions.availableMoves import AvailableMoves
from functions.applyMove import ApplyMove
from functions.compareStates import CompareStates
from functions.normalization import Normalization
import sys


def print_state(file_path):
    """
    Reads and prints the state from the given file.
    """
    try:
        # Create an instance of the StateRepresentation class
        state = StateRepresentation(file_path)
        state.read_file()  # Read the file
        state.print_state()  # Print the state
    except Exception as e:
        print(f"Error in printing state: {e}")

def done_state(file_path):
    """
    Return True if the puzzle is solved, else False.
    """
    try:
        # Create an instance of the IdentifySolution class
        instance = IdentifySolution(file_path)
        instance.state.read_file()  # Read the file
        is_puzzle_solved = instance.puzzleSolved()
        print(is_puzzle_solved)
    except Exception as e:
        print(f"Error in done state: {e}")

def available_moves(file_path):
    """
    Return all the moves available in the puzzle.
    """
    try:
        # Create an instance of the AvailableMoves class
        instance = AvailableMoves(file_path)
        instance.state.read_file()  # Read the file
        moves = instance.get_available_moves()  # Get available moves
        if moves:
            print("Available Moves:")
            for move in moves:
                print(move)
        else:
            print("No available moves.")
    except Exception as e:
        print(f"Error in available moves state: {e}")

def apply_move(file_path, move):
    """
    Apply the move if possible and return the new state of the puzzle.
    """
    try:
        # Create an instance of the ApplyMove class
        instance = ApplyMove(file_path, move)
        instance.apply_move()  # Apply the move
    except Exception as e:
        print(f"Error in applying move: {e}")

def identify_identical(file1, file2):
    """
    Return True if the two states are identical, else False.
    """
    try:
        # Create an instance of the StateRepresentation class for both states
        state1 = StateRepresentation(file1)
        state2 = StateRepresentation(file2)
        compareStates = CompareStates()

        # Read the files
        state1.read_file()
        state2.read_file()

        # Compare the states
        isIdentical = compareStates.compare_states(state1.grid, state2.grid)
        print(isIdentical)
    except Exception as e:
        print(f"Error in identifying identical states: {e}")

def standardize_input(input):
    # Strip spaces and handle other formatting issues
    input = input.replace(", ", ",").replace(" ,", ",")
    return input

def normalize_input(file):
    # read file and take instance of StateRepresentation
    state_representation = StateRepresentation(file)
    state_representation.read_file()
    
    # pass grid matrix to Normalization class
    instance = Normalization(state_representation.grid)
    
    # get normalized matrix
    normalized_matrix = instance.normalize_matrix() 
    # print normalized matrix
    state_representation.dynamic_print_state(normalized_matrix)

def main():
    """
    Main function to handle all actions.
    """
    if len(sys.argv) < 3:
        print("Usage:")
        print("python3 main.py print <file_path>")
        print("python3 main.py done <file_path>")
        print("python3 main.py availableMoves <file_path>")
        print("python3 main.py applyMove <file_path> <move>")
        print("python3 main.py compare <file_path1> <file_path2>")
        print("python3 main.py norm <file_path1>")
        sys.exit(1)

    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "print":
        print_state(file_path)
    elif action == "done":
        done_state(file_path)
    elif action == "availableMoves":
        available_moves(file_path)
    elif action == "applyMove":
        if len(sys.argv) < 4:
            print("Error: Missing move for applyMove.")
            print("Example: python3 main.py applyMove <file_path> \"(3, down)\"")
            sys.exit(1)
        move = sys.argv[3]
        move = standardize_input(move)
        apply_move(file_path, move)
    elif action == "compare":
        if len(sys.argv) < 4:
            print("Error: Missing file paths for comparison.")
            print("Example: python3 main.py compare <file_path1> <file_path2>")
            sys.exit(1)
        file_path1 = sys.argv[2]
        file_path2 = sys.argv[3]
        identify_identical(file_path1, file_path2)
    elif action == "norm":
        normalize_input(file_path)
    else:
        print(f"Invalid action: {action}")
        print("Supported actions: print, done, availableMoves, applyMove, compare")
        sys.exit(1)

if __name__ == "__main__":
    main()
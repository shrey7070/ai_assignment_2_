import copy
from functions.state_representation import StateRepresentation

class ApplyMove:
    def __init__(self, file_path, move):
        self.state = StateRepresentation(file_path)  # Instance of StateRepresentation
        self.state.read_file()  # Read the file
        self.move = move  # Move to be applied
    def apply_move(self):
        
        # Remove the parentheses
        move = self.move.strip("()")
        '''
        key added based on output of available moves, so while adding command line arguments, we can copy them
        to check apply_move and use them in command line arguments
        '''
        directions = {
            "'down'": (1, 0),
            "'up'": (-1, 0),
            "'right'": (0, 1),
            "'left'": (0, -1),
        }
        
        # Split the string by the comma
        value, direction = move.split(",")
        direction = direction.strip()  # Ensure there are no extra spaces
        # clone the state for future use
        new_state = copy.deepcopy(self.state.grid)
        # Variables to store the starting position to update the state
        start_row, start_col = None, None

        # Find the starting position of the value
        for row in range(self.state.rows):
            for col in range(self.state.cols):
                if new_state[row][col] == value:
                    start_row, start_col = row, col
                    # print(col)
                    # print(start_row)
                    # print(row)
                    break
            if start_row is not None:  # Exit the outer loop if position is found
                break

        if start_row is None or start_col is None:
            print("Error: Value not found in the grid.")
            return

        # Apply the move
        new_row = start_row + directions[direction][0]
        new_col = start_col + directions[direction][1]

        # Validate the new position
        if 0 <= new_row < self.state.rows and 0 <= new_col < self.state.cols:
            if new_state[new_row][new_col] in ["0", "-1"]:  # Valid destination
                # Update the grid
                # Mark the original position as empty
                new_state[start_row][start_col] = "0"  
                # Move the value
                new_state[new_row][new_col] = value
                self.state.dynamic_print_state(new_state)
            else:
                print("Error: Destination is blocked.")
        else:
            print("Error: Move out of bounds.")
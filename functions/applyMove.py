import copy
from functions.state_representation import StateRepresentation
from helper import DIRECTIONS

class ApplyMove:
    def __init__(self,grid,move,rows,cols):
        # self.state = StateRepresentation()  # Instance of StateRepresentation
        self.move = move # Move to be applied
        self.grid = grid # Grid to be applied
        self.rows = rows # Number of rows
        self.cols = cols # Number of cols
    def apply_move(self):
        move = self.move.strip("()")
        value, direction = move.split(",")
        direction = direction.strip()
        
        # clone the state for future use
        new_state = copy.deepcopy(self.grid)

        # Find all starting positions of the value
        positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                if new_state[row][col] == value and value not in ["1", "0", "-1"]:
                    positions.append({"start_row": row, "start_col": col})

        # Check if positions list is empty
        if not positions:
            print("Error: Value not found in the grid.")
            return
        
        ''' 
            if user wants to move to position Right, then we have to reverse the positions
            to get the correct order of moves. otherwise it will move only single value of block.
        '''
        if direction == "right" or direction == "down":
            positions = positions[::-1]

        # Iterate over all positions
        for pos in positions:
            start_row, start_col = pos["start_row"], pos["start_col"]
            
            # Calculate the new position based on the move direction
            new_row = start_row + DIRECTIONS[direction][0]
            new_col = start_col + DIRECTIONS[direction][1]

            # Validate the new position
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if new_state[new_row][new_col] in ["0", "-1"]:  # Check valid destination
                    if new_state[new_row][new_col] == '-1' and new_state[start_row][start_col] == "2":
                        new_state[start_row][start_col] = "0"
                        new_state[new_row][new_col] = value
                    else:
                        new_state[start_row][start_col] = "0"
                        new_state[new_row][new_col] = value
                else:
                    print(f"Destination ({new_row}, {new_col}) is blocked.")
            else:
                print(f"Move out of bounds for value {value} from ({start_row}, {start_col}) to ({new_row}, {new_col}).")
        return new_state
import sys
from functions.state_representation import StateRepresentation

class AvailableMoves:
    file_path = sys.argv[1]
    def __init__(self, file_path):
        self.state = StateRepresentation(file_path) # instance of StateRepresentation
        self.state.read_file() #read the file
    
    # check available moves
    def get_available_moves(self):
        '''
        Returns a dict of available moves for the puzzle.
        '''
        available_moves = []
        ''' 
        down: (1,0) = Move 1 row down, no change in the column.
        up: (-1,0) = Move 1 row up, no change in the column.
        right: (0,1) = Move 1 col right, no change in the row.
        left: (0,-1) = Move 1 col left, no change in the row.
        '''
        directions = {
            "down": (1, 0),
            "up": (-1, 0),
            "right": (0, 1),
            "left": (0, -1),
        }

        for row in range(self.state.rows):
            for col in range(self.state.cols):
                ''' 
                1 is wall (not movable), 0 is empty, -1 is goal state.
                so we will skip moving them and focus on other values.
                '''
                if self.state.grid[row][col] == "" or self.state.grid[row][col] == "1" or self.state.grid[row][col] == "0":
                    continue
                # Check all possible directions (up, down, left, right)
                for direction, (row_offset, col_offset) in directions.items():
                    # Calculate the new position after moving in this direction
                    new_row = row + row_offset
                    new_col = col + col_offset
                    '''
                    if new_row and new_col indexes values are equal to 0 then move or -1
                    '''
                    if 0 <= new_row < self.state.rows and 0 <= new_col < self.state.cols:
                        if self.state.grid[new_row][new_col] in ["0", "-1"]:
                            available_moves.append((int(self.state.grid[row][col]), direction))
        return available_moves
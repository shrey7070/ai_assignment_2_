from functions.state_representation import StateRepresentation
from helper import DIRECTIONS

class AvailableMoves:
    def get_available_moves(self, grid, rows, cols):
        available_moves = []
        visited = set()  # To track visited block

        def get_connected_blocks(r, c, value):
            """
            Perform DFS to find all connected block with the same value.
            """
            stack = [(r, c)]
            connected = set()
            while stack:
                x, y = stack.pop()
                if (x, y) not in visited and 0 <= x < rows and 0 <= y < cols and grid[x][y] == value:
                    visited.add((x, y))
                    connected.add((x, y))
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        stack.append((x + dx, y + dy))
            return connected

        for row in range(rows):
            for col in range(cols):
                current_value = grid[row][col]

                # Skip if it's already visited or not a movable block
                if (row, col) in visited or current_value in ['', '1', '0', '-1']:
                    continue

                # Get all connected blocks for the current value
                connected_blocks = get_connected_blocks(row, col, current_value)

                # Check all possible moves for the entire block
                for direction, (row_offset, col_offset) in DIRECTIONS.items():
                    can_move = True
                    for r, c in connected_blocks:
                        new_row = r + row_offset
                        new_col = c + col_offset
                        
                        # Check if the new position is within bounds
                        if not (0 <= new_row < rows and 0 <= new_col < cols):
                            can_move = False
                            break

                        new_value = grid[new_row][new_col]
                        # Check if the new cell is part of the connected_blocks or the value is allowed
                        if current_value == "2":
                            if (new_value not in ["0", "-1"] and 
                                (new_row, new_col) not in connected_blocks):
                                can_move = False
                                break
                        else:
                            if (new_value != "0" and 
                                (new_row, new_col) not in connected_blocks):
                                can_move = False
                                break

                    # If the entire block can move, add the move
                    if can_move:
                        move = f"({int(current_value)},{direction})"
                        if move not in available_moves:
                            available_moves.append(move)
        return available_moves
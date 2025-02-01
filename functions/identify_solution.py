class IdentifySolution:
    @staticmethod
    def puzzleSolved(grid, rows, cols):
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "-1":  # Check for the presence of "-1" as -1 is goal state
                    return False  # Puzzle is not solved
        return True # Puzzle is solved
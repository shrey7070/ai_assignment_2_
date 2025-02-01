class StateRepresentation:
    def __init__(self, fileName):
        self.fileName = fileName
        self.rows = 0
        self.cols = 0
        self.grid = []
        self.content = [] # adding here for getting an list of rows and columns for other functions
    
    def read_file(self):
        try:
            with open(self.fileName, 'r') as file:
                self.content = file.readlines()
            
            dimensions = self.content[0].strip().split(',')
            self.cols, self.rows = int(dimensions[0]), int(dimensions[1])

            for line in self.content[1:]:
                split_lines = line.strip().split(',')
                self.grid.append(split_lines)

        # error if file does not exist
        except FileNotFoundError:
            print(f"File '{self.fileName}' not found.")
        
        # error if format is not proper
        except ValueError:
            print(f"Invalid format in file '{self.fileName}'.")
    
    # Print State and Grid dimensions
    def print_state(self):
        # Prints the grid representation of the state.
        print(self.cols,',',self.rows)
        for row in self.grid:
            print(' '.join(row))
    
    # Print copied State and Grid for given state in parameter
    def dynamic_print_state(self, state):
        # Prints the grid representation of the state.
        print(self.cols,',',self.rows)
        for row in state:
            print(' '.join(str(item) for item in row))

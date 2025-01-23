import sys
from functions.state_representation import StateRepresentation

class IdentifySolution:
    file_path = sys.argv[1]
    def __init__(self, file_path):
        self.state = StateRepresentation(file_path) # instance of StateRepresentation
        self.state.read_file() #read the file
    def puzzleSolved(self):
        for line in self.state.content[1:]:
            split_lines = line.strip().split(',')
            if "-1" in split_lines:
                return False
        return True
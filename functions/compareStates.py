class CompareStates:
    @staticmethod
    def compare_states(state1, state2):
        # Check if dimensions match
        if len(state1) != len(state2) or len(state1[0]) != len(state2[0]):
            return False

        # Compare each element
        for row in range(len(state1)):
            for col in range(len(state1[0])):
                if state1[row][col] != state2[row][col]:
                    return False
        return True

class Normalization:
    def __init__(self, matrix):
        self.matrix = matrix

    def swap_indices(self, idx1, idx2):
        """
        Swap two indices in the matrix.
        """
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                # print("================================")
                # print(self.matrix[i][j] == 12)
                # print(idx1 == 12)
                # print("================================")
                if self.matrix[i][j] == str(idx1):
                    self.matrix[i][j] = str(idx2)
                elif self.matrix[i][j] == str(idx2):
                    self.matrix[i][j] = str(idx1)
    def normalize_matrix(self):
        """
        Normalize the matrix so that each brick uses the smallest possible index.
        """
        # print("Initial Matrix:")
        # for row in self.matrix:
        #     print(' '.join(map(str, row)))
        next_idx = 3  # 1(wall) and 2(target brick) are reserved
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                try:
                    current_value = int(self.matrix[i][j])
                except ValueError:
                    continue
                if current_value == next_idx:
                    next_idx += 1
                else:
                    if current_value > next_idx: 
                        self.swap_indices(current_value,next_idx)
                        next_idx += 1

        return self.matrix
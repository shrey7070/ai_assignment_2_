class Normalization:
    def __init__(self, matrix):
        self.matrix = matrix

    def swap_indexes(self, index1, index2):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == str(index1):
                    self.matrix[i][j] = str(index2)
                elif self.matrix[i][j] == str(index2):
                    self.matrix[i][j] = str(index1)
    def normalize_matrix(self):
        next_idx = 3  # 1(wall) and 2(target block) are reserved
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
                        self.swap_indexes(current_value,next_idx)
                        next_idx += 1

        return self.matrix
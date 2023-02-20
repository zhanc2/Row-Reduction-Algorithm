

class Matrix:
    def __init__(self, dimensions: int, matrix: list = None):
        self.dimensions = dimensions
        self.matrix = [[None]*dimensions]*dimensions if matrix is None else matrix if self.check_valid(matrix) else None

    @staticmethod
    def check_valid(matrix):
        length = len(matrix[0])
        for i in matrix:
            if not len(i) == length:
                return False
        return True

    # def add_num(self):



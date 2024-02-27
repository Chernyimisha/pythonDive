class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def __str__(self):
        # result = '\n'.join(map(str, self.data))
        result = ''
        for row in self.data:
            result = result + ' '.join(map(str, row)) + '\n'
        return result.rstrip('\n')

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.data[i][j] != other.data[i][j]:
                        return False
        else:
            return False
        return True

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.data = [[0 for i in range(self.cols)] for j in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
        else:
            raise ValueError('Сложение матриц невозможно')
        return result

    def __mul__(self, other):
        if self.cols == other.rows:
            result = Matrix(self.cols, other.rows)
            result.data = [[0 for i in range(other.cols)] for j in range(self.rows)]
            print(result.data)
            for i in range(self.cols):
                for j in range(self.rows):
                    summ = 0
                    for k in range(other.rows):
                        summ += self.data[j][k] * other.data[k][i]
                    result.data[j][i] = summ
        else:
            raise ValueError('Умножение матриц невозможно')
        return result

if __name__ == '__main__':

    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[1, 2, 3], [4, 9, 6]]

    print(matrix1)
    print(matrix2)
    print(repr(matrix1))
    print(matrix1 == matrix2)
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

# Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)


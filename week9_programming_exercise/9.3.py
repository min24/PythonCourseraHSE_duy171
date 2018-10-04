from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = copy.deepcopy(matrix1)
        self.matrix2 = copy.deepcopy(matrix2)


class Matrix:
    def __init__(self, arr):
        self.arr = copy.deepcopy(arr)

    def __str__(self):
        result = ''
        if len(self.arr) != 0:
            if isinstance(self.arr[0], list):
                for i in self.arr:
                    i = map(str, i)
                    result1 = '\t'.join(i)
                    result += result1 + '\n'
            elif isinstance(self.arr[0], int):
                for i in self.arr:
                    result += str(i) + '\t'
            elif isinstance(self.arr[0], float):
                for i in self.arr:
                    result += str(i) + '\t'
        else:
            result = '\t'
        return result[:-1]

    def size(self):
        return (len(self.arr), len(self.arr[0]))

    def __add__(self, other):
        result = []
        if Matrix.size(Matrix(self.arr)) == Matrix.size(Matrix(other.arr)):
            for i, j in zip(self.arr, other.arr):
                result1 = [x+y for x, y in zip(i, j)]
                result += [result1]
            return Matrix(result)
        else:
            error = MatrixError(self, other)
            raise error

    def __mul__(self, alpha):
        result = copy.deepcopy(self.arr)
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] *= alpha
        return Matrix(result)

    def transpose(self):
        result = list(zip(*self.arr))
        result = list(map(list, result))
        self.arr = result
        return Matrix(result)

    def transposed(self):
        result = list(zip(*self.arr))
        result = list(map(list, result))
        return Matrix(result)

    __rmul__ = __mul__

exec(stdin.read())

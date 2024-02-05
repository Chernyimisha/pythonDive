# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы
# matrix, и возвращает транспонированную матрицу.

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# matrix = [[1]]


# def transpose(matrix: matrix) -> matrix:
#     result = []
#     temp = []
#     length = len(matrix)
#     for i in range(length):
#         for j in range(length):
#             temp.append(matrix[j][i])
#         result.append(temp)
#         temp = []
#     return result
#
#
# transposed_matrix = transpose(matrix)
# print(transposed_matrix)

def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transpose(matrix))
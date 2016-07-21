class ShapeError(Exception):
    pass


def shape(vector):
    if is_matrix(vector):
        return (len(vector), len(vector[0]))
    return (len(vector), )

def is_matrix(array):
    if type(array[0]) == list:
        return True

def compare_shape(*args):
    if len(set([shape(item) for item in args])) != 1:
        raise ShapeError

def vector_add(vector, vector2):
    compare_shape(vector, vector2)
    #return [vector[index] + vector2[index] for index in range(len(vector))]
    return [sum(values) for values in zip(vector, vector2)]

def vector_sub(vector, vector2):
    compare_shape(vector, vector2)
    return [item1 - item2 for item1, item2 in zip(vector, vector2)]

def vector_sum(*args):
    compare_shape(*args)
    return [sum(values) for values in zip(*args)]

def dot(vector, vector2):
    compare_shape(vector, vector2)
    return sum([item1 * item2 for item1, item2 in zip(vector, vector2)])

def vector_multiply(vector, number):
    return [item * number for item in vector]

def vector_mean(*args):
    return [sum(values)/len(values) for values in zip(*args)]

def magnitude(vector):
    return sum([item ** 2 for item in vector])**.5

def matrix_row(matrix, row):
    return matrix[row]

def matrix_col(matrix, col):
    return [vector[col] for vector in matrix]

def matrix_add(matrix, matrix2):
    compare_shape(matrix, matrix)
    return [vector_add(item1, item2) for item1, item2 in zip(matrix, matrix2)]

def matrix_sub(matrix, matrix2):
    compare_shape(matrix, matrix)
    return [vector_sub(item1, item2) for item1, item2 in zip(matrix, matrix2)]

def matrix_scalar_multiply(matrix, number):
    return [vector_multiply(item1, number) for item1 in matrix]

def matrix_vector_multiply(matrix, vector):
    compare_shape(matrix_row(matrix, 0), vector)
    return [dot(item1, vector) for item1 in matrix]

def matrix_matrix_multiply(matrix, matrix2):
    compare_shape(matrix_row(matrix, 0), matrix_col(matrix2, 0))
    #This is rough, I'm gonna try to think this one into something cleaner
    return [[dot(matrix_row(matrix, item1), matrix_col(matrix2, item2))
        for item2 in range(len(matrix_row(matrix2, 0)))]
        for item1 in range(len(matrix_col(matrix, 0)))]

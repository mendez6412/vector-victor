# class LinearAlgebra:
#     def __init__(self, vector):
#         self.vector = vector
#
#     def shape(self):
class ShapeError(Exception):
    pass


def shape(vector):
    return (len(vector), )

def compare_shape(vector, vector2):
    if shape(vector) != shape(vector2):
        raise ShapeError

def vector_add(vector, vector2):
    compare_shape(vector, vector2)
    return [item1 + item2 for item1, item2 in zip(vector, vector2)]

def vector_sub(vector, vector2):
    compare_shape(vector, vector2)
    return [item1 - item2 for item1, item2 in zip(vector, vector2)]

def vector_sum(*args)

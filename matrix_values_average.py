"""
Given the following input

    Input
    1 2 3 4
    4 5 6 5
    7 8 9 6

we compute the sum of values along diagonals going from bottom left to top right.
We then replace each value in the matrix with the average of the sum along the
corresponding diagonal.

    1st Diagonal = 1
    2nd Diagonal = 2, 4
    3rd Diagonal = 3, 5, 7
    4th Diagonal = 4, 6, 8

    Average of sum along 3rd diagonal: 3 + 5 + 7 = 15/3 = 5

    Output
    1 3 5 6
    3 5 6 7
    5 6 7 6

"""

from collections import namedtuple

RowCol = namedtuple('RowCol', ['row', 'col'])

class DiagonalElements(object):
    def __init__(self, matrix, start_row, start_col):
        self.matrix = matrix

        self.start_row = start_row
        self.start_col = start_col

        self.row_count = len(matrix)
        self._elt_count = 0

    def __iter__(self):
        (row, col) = (self.start_row, self.start_col)

        while row < self.row_count and col >= 0:
            yield RowCol(row, col)
            self._elt_count += 1

            row += 1
            col -= 1

    def get_elt_count(self):
        return self._elt_count

class DiagonalOrigins(object):
    def __init__(self, matrix):
        self.matrix = matrix

        self.row_count = len(matrix)
        self.col_count = len(matrix[0])

    def __iter__(self):
        (row, col) = (0, 1)

        while col < self.col_count and row < self.row_count:
            yield RowCol(row, col)

            if col + 1 < self.col_count:
                col += 1
            else:
                row += 1

def compute_diagonal(matrix, start_row, start_col):
    diagonal_elts_iter = DiagonalElements(matrix, start_row, start_col)

    sum = reduce(lambda s, rc: s + matrix[rc.row][rc.col], diagonal_elts_iter, 0)

    iter_elt_count = diagonal_elts_iter.get_elt_count()

    diagonal_elt = sum / iter_elt_count

    for rc in diagonal_elts_iter:
        matrix[rc.row][rc.col] = diagonal_elt

def modify(matrix):
    for (row, col) in DiagonalOrigins(matrix):
        compute_diagonal(matrix, row, col)

    print('modified: ', matrix)

modify([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 6]])

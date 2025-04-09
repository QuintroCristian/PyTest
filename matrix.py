class Matrix:
    """Clase que representa una matriz genérica y su manipulación básica."""
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._data = [[0 for _ in range(cols)] for _ in range(rows)]

    def fill(self, row, col, value):
        self._data[row][col] = value

    def get_data(self):
        return self._data

    def row_count(self):
        return self._rows

    def col_count(self):
        return self._cols

    def print_matrix(self):
        for row in self._data:
            print(row)
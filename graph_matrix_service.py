import ast
from matrix import Matrix

class GraphMatrixService:
    """
    Clase que maneja la lógica en la matriz de adyacencia
    vértices y aristas
    """

    def fill_undirected_graph(self, matrix: Matrix, num_vertices, num_edges, input_func):
        """
        Llena una matriz como grafo no dirigido.
        """
        matrix._data = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        for _ in range(num_edges):
            v1 = int(input_func("Ingrese vértice de origen: ")) - 1
            v2 = int(input_func("Ingrese vértice de destino: ")) - 1
            matrix.fill(v1, v2, 1)
            matrix.fill(v2, v1, 1)

        print("Matriz de adyacencia generada:")
        matrix.print_matrix()

    def fill_adjacency_matrix(self, matrix: Matrix, input_func):
        """
        se pide al usuario una matriz de adyacencia en formato de lista de listas.
        Luego, solicita
        los nombres de los vértices y muestra las aristas resultantes como
        pares ordenados.
        """
        user_matrix_str = input_func("Ingrese la matriz en formato [[0,1],[1,0]]: ")
        try:
            user_matrix = ast.literal_eval(user_matrix_str)
        except (SyntaxError, ValueError):
            print("Formato inválido. Intente nuevamente.")
            return

        rows = len(user_matrix)
        cols = len(user_matrix[0]) if rows > 0 else 0

        matrix._rows = rows
        matrix._cols = cols
        matrix._data = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                matrix.fill(i, j, user_matrix[i][j])

        vertex_names = []
        for i in range(rows):
            name = input_func(f"Ingrese el nombre para el vértice {i+1}: ")
            vertex_names.append(name)

        edges = []
        for i in range(rows):
            for j in range(cols):
                if matrix._data[i][j] == 1:
                    edges.append((vertex_names[i], vertex_names[j]))

        print("\nMatriz ingresada correctamente:")
        matrix.print_matrix()
        print("\nVértices:", vertex_names)
        print("Aristas como pares ordenados:", edges)
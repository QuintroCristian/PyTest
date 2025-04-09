from graph_matrix_service import GraphMatrixService
from matrix import Matrix

class Menu:
    """Clase encargada de manejar el menú y la interacción con el usuario."""
    def __init__(self, graph_service: GraphMatrixService, graph_matrix: Matrix):
        self._graph_service = graph_service
        self._graph_matrix = graph_matrix

    def display_menu(self, input_fn):
        option = input_fn("Seleccione (1-Matriz de adyacencia, 2-Vértices y aristas): ")
        if option == '1':
            self._graph_service.fill_adjacency_matrix(self._graph_matrix, input_fn)
        elif option == '2':
            try:
                vertices = int(input_fn("Ingrese la cantidad de vértices: "))
                edges = int(input_fn("Ingrese la cantidad de aristas: "))
                self._graph_service.fill_undirected_graph(self._graph_matrix, vertices, edges, input_fn)
            except ValueError:
                print("Por favor ingrese números válidos.")
        else:
            print("Opción inválida")


def safe_input(prompt):
    try:
        return input(prompt)
    except Exception as e:
        print(f"Error: {e}")
        return ""
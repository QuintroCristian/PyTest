from matrix import Matrix
from graph_matrix_service import GraphMatrixService
from menu import Menu

def safe_input(prompt):
    try:
        return input(prompt)
    except Exception as e:
        print(f"Error: {e}")
        return ""

class MainApp:
    """Clase principal que orquesta la ejecución de la aplicación."""

    def __init__(self):
        self.matrix = Matrix(3, 3)
        self.matrix_service = GraphMatrixService()
        self.menu = Menu(self.matrix_service, self.matrix)

    def run(self):
        """Inicia el flujo de la aplicación."""
        self.menu.display_menu(safe_input)

if __name__ == "__main__":
    app = MainApp()
    app.run()


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import matplotlib.pyplot as plt
from node import *
from segment import *
from graph import *


class GraphInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Interface")

        self.graph = Graph()
        self.mode = None
        self.selected_node = None

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.mpl_connect("button_press_event", self.on_click)

        control_frame = tk.Frame(root)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Button(control_frame, text="Cargar ejemplo", command=self.load_example).pack(pady=5)
        tk.Button(control_frame, text="Cargar desde .txt", command=self.load_from_file).pack(pady=5)
        tk.Button(control_frame, text="Guardar en .txt", command=self.save_to_file).pack(pady=5)
        tk.Button(control_frame, text="Añadir nodo", command=lambda: self.set_mode("add_node")).pack(pady=5)
        tk.Button(control_frame, text="Añadir segmento", command=lambda: self.set_mode("add_segment")).pack(pady=5)
        tk.Button(control_frame, text="Eliminar nodo", command=self.delete_node).pack(pady=5)
        tk.Button(control_frame, text="Nuevo grafo", command=self.new_graph).pack(pady=5)
        tk.Button(control_frame, text="Mostrar vecinos", command=self.plot_neighbors).pack(pady=5)

        self.draw()

    def draw(self):
        self.ax.clear()
        for segment in self.graph.segments:
            x_vals = [segment.origin.x, segment.destination.x]
            y_vals = [segment.origin.y, segment.destination.y]
            self.ax.plot(x_vals, y_vals, 'gray')
            mid_x = (x_vals[0] + x_vals[1]) / 2
            mid_y = (y_vals[0] + y_vals[1]) / 2
            self.ax.text(mid_x, mid_y, f"{segment.cost:.1f}", color='red', fontsize=8, ha='center')

        for node in self.graph.nodes:
            self.ax.plot(node.x, node.y, 'o')
            self.ax.text(node.x + 0.1, node.y + 0.1, node.name, fontsize=9)

        self.ax.set_title("Graph Viewer")
        self.ax.grid(True)
        self.canvas.draw()

    def set_mode(self, mode):
        self.mode = mode
        self.selected_node = None

    def get_node_at(self, x, y, tolerance=0.5):
        for node in self.graph.nodes:
            if abs(node.x - x) < tolerance and abs(node.y - y) < tolerance:
                return node
        return None

    def on_click(self, event):
        if event.inaxes != self.ax:
            return
        x, y = event.xdata, event.ydata
        clicked_node = self.get_node_at(x, y)

        if self.mode == "add_node":
            name = simpledialog.askstring("Nombre del nodo", "Introduce el nombre del nodo:")
            if name:
                new_node = Node(name, x, y)
                if AddNode(self.graph, new_node):
                    self.draw()
                else:
                    messagebox.showwarning("Error", "Ya existe un nodo con ese nombre.")

        elif self.mode == "add_segment":
            if not clicked_node:
                messagebox.showinfo("Info", "Haz clic sobre un nodo válido.")
                return

            if self.selected_node is None:
                self.selected_node = clicked_node
            elif clicked_node != self.selected_node:
                success = AddSegment(self.graph, self.selected_node.name, clicked_node.name)
                if success:
                    self.draw()
                else:
                    messagebox.showwarning("Error", "No se pudo añadir el segmento.")
                self.selected_node = None
            else:
                # Clic en el mismo nodo, reiniciamos
                self.selected_node = None

    def load_example(self):
        from test_graph import CreateGraph_1
        self.graph = CreateGraph_1()
        self.draw()

    def load_from_file(self):
        path = filedialog.askopenfilename(title="Selecciona archivo .txt", filetypes=[("Text files", "*.txt")])
        if path:
            self.graph = load_graph_from_file(path)
            self.draw()

    def save_to_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if path:
            save_graph_to_file(self.graph, path)
            messagebox.showinfo("Guardado", "Grafo guardado correctamente.")

    def delete_node(self):
        name = simpledialog.askstring("Eliminar nodo", "Introduce el nombre del nodo a eliminar:")
        if name:
            self.graph.nodes = [n for n in self.graph.nodes if n.name != name]
            self.graph.segments = [s for s in self.graph.segments if s.origin.name != name and s.destination.name != name]
            self.draw()

    def new_graph(self):
        self.graph = Graph()
        self.draw()

    def plot_neighbors(self):
        name = simpledialog.askstring("Mostrar vecinos", "Introduce el nombre del nodo:")
        if not name:
            return

        origin_node = None
        for node in self.graph.nodes:
            if node.name == name:
                origin_node = node
                break

        if not origin_node:
            messagebox.showerror("Error", "Nodo no encontrado")
            return

        self.ax.clear()

        for node in self.graph.nodes:
            color = 'blue' if node == origin_node else 'green' if node in origin_node.neighbors else 'gray'
            self.ax.plot(node.x, node.y, 'o', color=color)
            self.ax.text(node.x + 0.1, node.y + 0.1, node.name, fontsize=9)

        for segment in self.graph.segments:
            if segment.origin == origin_node or segment.destination == origin_node:
                x_vals = [segment.origin.x, segment.destination.x]
                y_vals = [segment.origin.y, segment.destination.y]
                self.ax.plot(x_vals, y_vals, 'red')
                mid_x = (x_vals[0] + x_vals[1]) / 2
                mid_y = (y_vals[0] + y_vals[1]) / 2
                self.ax.text(mid_x, mid_y, f"{segment.cost:.1f}", color='red', fontsize=8, ha='center')

        self.ax.set_title(f"Vecinos de {name}")
        self.ax.grid(True)
        self.canvas.draw()


# Lanzar la interfaz directamente
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphInterface(root)
    root.mainloop()

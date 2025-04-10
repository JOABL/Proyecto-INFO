import tkinter as tk
from tkinter import filedialog
from graph import *
from test_graph import *
import matplotlib.pyplot as plt
root = tk.Tk()
root.title("Graph Interface")
frame = tk.Frame(root)
frame.pack(pady=20)
current_graph = None
def show_example_graph():
    global current_graph
    current_graph = CreateGraph_1()
    Plot(current_graph)
def load_graph_from_file():
    global current_graph
    filename = filedialog.askopenfilename(title="Select Graph File", filetypes=[("Text Files", "*.txt")])
    if filename:
        current_graph = LoadGraphFromFile(filename)
        Plot(current_graph)
def show_neighbors():
    if current_graph is None:
        return
    node_name = node_entry.get()
    if not node_name:
        return
    success = PlotNode(current_graph, node_name)
    if not success:
        status_label.config(text=f"Node '{node_name}' not found!", fg="red")
    else:
        status_label.config(text=f"Showing neighbors of '{node_name}'", fg="green")
btn_example_graph = tk.Button(frame, text="Show Example Graph", command=show_example_graph)
btn_example_graph.pack(pady=5)
btn_load_graph = tk.Button(frame, text="Load Graph from File", command=load_graph_from_file)
btn_load_graph.pack(pady=5)
node_entry = tk.Entry(frame)
node_entry.pack(pady=5)
btn_show_neighbors = tk.Button(frame, text="Show Neighbors", command=show_neighbors)
btn_show_neighbors.pack(pady=5)
status_label = tk.Label(frame, text="", fg="black")
status_label.pack(pady=10)

root.mainloop()

# interface.py
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import *
import matplotlib.pyplot as plt

class GraphApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Editor")
        self.graph = Graph()
        self.selected_node = None

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master)
        self.canvas.get_tk_widget().pack()

        self.canvas.mpl_connect('button_press_event', self.on_click)

        # Botones
        tk.Button(master, text="Nuevo Grafo", command=self.new_graph).pack(side=tk.LEFT)
        tk.Button(master, text="Guardar", command=self.save_graph).pack(side=tk.LEFT)
        tk.Button(master, text="Cargar", command=self.load_graph).pack(side=tk.LEFT)
        tk.Button(master, text="Borrar Nodo", command=self.delete_node).pack(side=tk.LEFT)




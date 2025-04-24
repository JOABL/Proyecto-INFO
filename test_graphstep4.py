from graph import *
print ("Probando el grafo...")
G = LoadGraphFromFile("graph_data.txt")
Plot(G)

PlotNode(G, "A")

n = GetCloset(G, 8, 19)
print(f"Nodo más cercano a (8,19): {n.name}")
from graph import *
from path import *
g = LoadGraphFromFile("mapa.txt")
camino = FindShortestPath(g, "A", "F")

if camino:
    print("Camino más corto:")
    for node in camino.nodes:
        print(node.name, end=" -> ")
    print("FIN")
    fig, ax = plt.subplots()
    PlotPath(g, camino,ax)
    plt.show()
else:
    print("No hay camino.")
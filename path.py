from node import *
from graph import *
class CaminoMasCorto:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes=[]
        self.nodes=nodes
def AddNodeToPath(path,node):
    path.nodes.append(node)

def ContainsNode(path, node):
    return node in path.nodes
def CostToNode(path,node):
    if node not in path.nodes:
        return -1
    total=0
    for i in range(len(path.nodes)-1):
        total+=Distance(path.nodes[i],path.nodes[i+1])
        if path.nodes[i+1]==node:
            break
    return total

def PlotPath(graph, path, ax):
    for i in range(len(path.nodes) - 1):
        origen = path.nodes[i]
        destino = path.nodes[i + 1]


        for segment in graph.segments:
            if (segment.origin == origen and segment.destination == destino) or \
               (segment.origin == destino and segment.destination == origen):
                x_vals = [segment.origin.x, segment.destination.x]
                y_vals = [segment.origin.y, segment.destination.y]
                ax.plot(x_vals, y_vals, color='blue', linewidth=2.5)
                break





import matplotlib.pyplot as plt
import numpy as np
from node import *
from segment import*
class Graph:
    def __init__(self):
        self.nodes=[]
        self.segments=[]
def AddNode(g,n):
    if n in g.nodes:
        return False
    g.nodes.append(n)
    return True
def AddSegment(g, nameSegment, nameOriginNode, nameDestinationNode):
    origin = None
    destination = None
    for node in g.nodes:
        if node.name == nameOriginNode:
            origin = node
        if node.name == nameDestinationNode:
            destination = node

    if origin is None or destination is None:
        return False

    segment = Segment(nameSegment, origin, destination)
    g.segments.append(segment)

    AddNeighbor(origin, destination)
    return True

def GetCloset(g,x,y):
    closest_node=None
    closest_distance=float("inf")
    for node in g.nodes:
        temp_node=Node("temp",x,y)
        distance=Distance(temp_node,node)
        if distance<closest_distance:
            closest_distance=distance
            closest_node=node
    return closest_node

def Plot(g):
    fig, ax = plt.subplots()

    for node in g.nodes:
        ax.plot(node.x, node.y, 'o')
        ax.text(node.x + 0.1, node.y + 0.1, node.name, fontsize=12)

    for segment in g.segments:

        x_values = [segment.origin.x, segment.destination.x]
        y_values = [segment.origin.y, segment.destination.y]

        ax.plot(x_values, y_values, 'b-' )

        mid_x = (segment.origin.x + segment.destination.x) / 2
        mid_y = (segment.origin.y + segment.destination.y) / 2
        ax.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color='red', ha='center')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Graph Visualization')
    plt.grid(True)
    plt.show()
def PlotNode(g,nameOrigin):
    origin_node = None
    for node in g.nodes:
        if node.name == nameOrigin:
            origin_node = node
            break

    if origin_node is None:
        return False

    fig, ax = plt.subplots()

    for node in g.nodes:
        if node == origin_node:
            ax.plot(node.x, node.y, 'bo')
        elif node in origin_node.neighbors:
            ax.plot(node.x, node.y, 'go')
        else:
            ax.plot(node.x, node.y, 'ko')
        ax.text(node.x + 0.1, node.y + 0.1, node.name, fontsize=10)


    for neighbor in origin_node.neighbors:
        ax.plot([origin_node.x, neighbor.x], [origin_node.y, neighbor.y], 'r-')

        mid_x = (origin_node.x + neighbor.x) / 2
        mid_y = (origin_node.y + neighbor.y) / 2
        cost = Distance(origin_node, neighbor)
        ax.text(mid_x, mid_y, f"{cost:.2f}", fontsize=10, color='red', ha='center')

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title(f'Graph Visualization: {nameOrigin} and Neighbors')
    plt.grid(True)
    plt.show()

    return True


def LoadGraphFromFile(filename):
    g = Graph()

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if parts[0] == "Node":
                name, x, y = parts[1], float(parts[2]), float(parts[3])
                AddNode(g, Node(name, x, y))

            elif parts[0] == "Segment":
                name, origin, destination = parts[1], parts[2], parts[3]
                AddSegment(g, name, origin, destination)

    return g


from node import *
class Segment:
    def __init__(self,name:str,origin: Node,destination: Node):
        self.name=name
        self.origin=origin
        self.destination=destination
        self.cost=Distance(origin,destination)
def repr_segmento(segment):
    return f"Segment({segment.name}, from {segment.origin.name} to {segment.destination.name}, cost={segment.cost:.2f})"
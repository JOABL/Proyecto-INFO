from segment import *
from node import *
n1= Node("Kilian",0,0)
n2=Node("Cucu",3,4)
n3=Node("Raya",7.8,5.2)
segmento1=Segment("S1",n1,n2)
segmento2=Segment("S2",n2,n3)
print(repr_segmento(segmento1))
print(repr_segmento(segmento2))

# Desafio URI - BeeCrowd 1015.
# "Distance Between Two Points"
import math
x1, y1 = list(map(float,input().split()))
x2, y2 = list(map(float,input().split()))
distance = ((x2 - x1)**2) + ((y2 - y1)**2)
raiz = math.sqrt(distance)
print(f"{raiz:.4f}")
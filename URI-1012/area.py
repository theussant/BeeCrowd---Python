# Desafio URI - BeeCrowd 1012.
# "Area"
A, B, C = list(map(float,input().split()))
T = (A * C) / 2
CI = 3.14159 * C**2
TR = (A + B) * C / 2
Q = B ** 2
R = A * B
print(f"TRIANGULO: {T:.3f}")
print(f"CIRCULO: {CI:.3f}")
print(f"TRAPEZIO: {TR:.3f}")
print(f"QUADRADO: {Q:.3f}")
print(f"RETANGULO: {R:.3f}")


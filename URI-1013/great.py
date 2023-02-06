# Desafio URI - BeeCrowd 1013.
# "The Greatest"
a, b, c = list(map(int,input().split()))
MAB = (a + b + abs(a - b)) / 2
MAB = (MAB + c + abs(MAB - c)) / 2
print(f"{MAB:.0f} eh o maior")
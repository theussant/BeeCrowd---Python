# Desafio URI - BeeCrowd 1010.
# "Simple Calculate"
produto1 = input("Digite o Código, Unidade e Preço:\n").split(" ")
produto2 = input("Digite o Código, Unidade e Preço:\n").split(" ")
pro1, un1, pre1 = produto1
pro2, un2, pre2 = produto2
final = (int(un1)*float(pre1)) + (int(un2)*float(pre2))
print("VALOR A PAGAR: R$ %0.2f" %final)

# Desafio URI - BeeCrowd 1018.
# "BankNotes"

N = int(input())

n = [100,50,20,10,5,2,1]

print(N)
for x in n:
    print("%i notas(s) de R$ %d,00"%((N/x),x))
    N %= (x)


#n100 = N // 100
#N = N - n100*100

#n50 = N // 50
#N = N - n50*50

#n20 = N // 20
#N = N - n20*20

#n10 = N // 10
#N = N - n10*10

#n5 = N // 5
#N = N - n5*5

#n2 = N // 2
#N = N - n2*2

#n1 = N // 1
#N = N - n1*1
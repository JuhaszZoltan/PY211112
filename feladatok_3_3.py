import random
lista = []

alap = 10
for i in range(20):
    szam = random.randint(alap, 99)
    alap = szam
    lista.append(szam)
print(lista)
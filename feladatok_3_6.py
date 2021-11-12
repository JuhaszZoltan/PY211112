import random

lista = []

while len(lista) < 50:
    szam = random.randint(10, 99)
    if szam not in lista:
        lista.append(szam)

lista.sort()
print(lista)
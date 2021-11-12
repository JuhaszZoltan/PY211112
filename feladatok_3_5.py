import random

lista_a = []
for i in range(50):
    lista_a.append(random.randint(5, 49) * 2 + 1)

lista_b = []
while len(lista_b) < 50:
    szam = random.randint(10, 99)
    if szam % 2 == 1:
        lista_b.append(szam)

print(lista_a)
print('-----')
print(lista_b)

if 13 in lista_a: print('benne van')
else: print('nincs benne')

if lista_b.__contains__(13): print('benne van')
else: print('nincs benne')

# eldöntés tételének algoritmusa
i = 0
while i < len(lista_a) and lista_a[i] != 13:
    i += 1
if i < len(lista_a):
    print('benne van')
else:
    print('nincs benne')
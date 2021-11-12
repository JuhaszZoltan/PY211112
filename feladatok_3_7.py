import random

# szelvény kitöltése:
print('töltsd ki a szelvényt:')
tippek_input = input('7db különböző szám, szóközzel elválasztva: ')
tippek = []
for t in tippek_input.split():
    tippek.append(int(t))

# szelvény validáció
valid = True

# TODO: ellenőrizni!!!

if len(tippek) != 7: valid = False
for i in range(len(tippek)):
    if tippek[i] > 35 or tippek[i] < 1:
        valid = False
    for j in range(len(tippek)):
        if tippek[i] == tippek[j] and i != j:
            valid = False

if valid:
    gepi_nyeroszamok = []
    kezi_nyeroszamok = []

    # gépi sorsolás:
    while len(gepi_nyeroszamok) < 7:
        n = random.randint(1, 35)
        if n not in gepi_nyeroszamok:
            gepi_nyeroszamok.append(n)

    # kézi sorsolás:
    while len(kezi_nyeroszamok) < 7:
        n = random.randint(1, 35)
        if n not in kezi_nyeroszamok:
            kezi_nyeroszamok.append(n)

    # rendezés kiírás előtt
    tippek.sort()
    gepi_nyeroszamok.sort()
    kezi_nyeroszamok.sort()

    print(f'szelvényed: {tippek}')
    print(f'gépi sorsolás: {gepi_nyeroszamok}')
    print(f'kézi sorsolás: {kezi_nyeroszamok}')


    # találatok megszámolása:
    gepi_talalat = 0
    for t in tippek:
        if t in gepi_nyeroszamok:
            gepi_talalat += 1

    kezi_talalat = 0
    for t in tippek:
        if t in kezi_nyeroszamok:
            kezi_talalat += 1

    print(f'gépi sorsoláson {gepi_talalat} találatod volt')
    print(f'kézi sorsoláson {kezi_talalat} találatod volt')

else: print('rosszul töltötted ki a szelvényt :(')

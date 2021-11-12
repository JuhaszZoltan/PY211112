nevek = []
szamlalo = 0

while szamlalo < 10:
    nev = input(f'{szamlalo + 1}. név: ')
    if nev == '': break
    nevek.append(nev)
    szamlalo += 1

print(nevek)
import random
zoldsegek = ['bab', 'krumpli', 'paprika', 'répa', 'retek', 'karalábé']
# összekeveri a lista elemeit
random.shuffle(zoldsegek)
print(zoldsegek)

szamok = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(szamok)
print(szamok)

# kiválaszt a listából véletlenszerű elemet
random_elem = random.choice(szamok)
print(valami)

# kiválaszt a listából k db elemet (ismétléssel!)
random_elemek = random.choices(szamok, k = 5)
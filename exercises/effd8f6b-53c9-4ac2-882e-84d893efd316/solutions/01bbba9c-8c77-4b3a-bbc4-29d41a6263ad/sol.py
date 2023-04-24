skaicius = int(input('Skaičius:\n')) 
kiekis = 0

for daliklis in range (skaicius-1, 1, -1):
    if skaicius % daliklis == 0:
        print(skaicius, 'dalinasi be liekanos iš', daliklis)
        kiekis += 1

print('Viso', skaicius, 'dalinosi be liekanos', kiekis, 'kart.')

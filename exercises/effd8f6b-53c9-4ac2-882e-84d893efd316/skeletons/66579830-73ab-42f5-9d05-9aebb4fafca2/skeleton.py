skaicius = int(input('Skaičius:\n')) 

for daliklis in range (skaicius-1, 1, -1):
    if skaicius % daliklis == 0:
        print(skaicius, 'dalinasi be liekanos iš', daliklis)

print('Viso', skaicius, 'dalinosi be liekanos', amount, 'kart.')
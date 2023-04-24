def vidurkis(*arg):
    suma = 0
    if len(arg) != 0:
        for skaicius in arg:
            suma += skaicius
        return suma/len(arg)
    
    return "argumentų kiekis = 0 ..."

print(vidurkis(*range(1, 100, 2)))
def vidurkis(*arg):
    suma = 0
    if len(arg) != 0:
        for skaicius in arg:
            suma += skaicius
        return suma/len(arg)
    return suma

### Do not change that code here ##### 
print(vidurkis(*map(int, input().split())))  
######################################

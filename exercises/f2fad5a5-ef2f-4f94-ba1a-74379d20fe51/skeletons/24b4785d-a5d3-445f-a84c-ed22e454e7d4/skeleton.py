# Dviejų parametrų laipsnio funkcijos pavyzdys.
def laipsniu(x, n):
    return x**n
    
'''  
print(3, '^', 4, 'yra:', laipsniu(3, 4))
print(4, '^', 3, 'yra:', laipsniu(4, 3))
print(3, '^', 4, 'yra:', laipsniu(x=3, n=4))
print(4, '^', 3, 'yra:', laipsniu(n=3, x=4))
#'''


# Jūsų šaknies funkcija
def saknis(x):
	return x**0.5

x = int(input())

# Tikėtinas rezultatas: n√x yra: (čia bus rezultatas)
print(str(2) + '\u221A' + x, 'yra:', saknis(x)) # Pakeisti

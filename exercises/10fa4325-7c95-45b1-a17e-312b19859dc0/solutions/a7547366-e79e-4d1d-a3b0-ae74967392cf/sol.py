tekstas = input('Tekstas?\n')
unikalus = set()
for i in tekstas:
    unikalus.update(i)
    
print(tekstas,'susideda iš', len(unikalus), 'simbolių.')
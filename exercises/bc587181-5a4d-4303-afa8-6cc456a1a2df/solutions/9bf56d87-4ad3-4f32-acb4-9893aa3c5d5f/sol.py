
class Figura():
    def perimetras(s):
       return sum(s.krastines)
    def __str__(s):
        return f'{s.__class__.__name__} {s.krastines}'

class Kvadratas(Figura):
    def __init__(s, a):
        s.a = a
        s.krastines = [s.a for i in range(4)]
    def plotas(s):
        return s.krastines[0]**2

class Staciakampis(Figura):
    def __init__(s, a, b):
        s.a = a
        s.b = b
        s.krastines = [s.a, s.b, s.a, s.b]
    def plotas(s):
        return s.krastines[0]*s.krastines[1]

class Trikampis(Figura):
    def __init__(s, a, b, c):
        s.a = a
        s.b = b
        s.c = c
        s.krastines = [s.a, s.b, s.c]
    def plotas(s):
        return (s.krastines[0]*s.krastines[1])/2

objektu_sarasas = [Kvadratas(7), Kvadratas(5, 6),  Trikampis(3, 4, 5)]
for objektas in objektu_sarasas:
    print(objektas, objektas.perimetras(), objektas.plotas())
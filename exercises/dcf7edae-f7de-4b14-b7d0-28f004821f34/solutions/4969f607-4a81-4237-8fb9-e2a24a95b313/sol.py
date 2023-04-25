class Staciakampis:
    a = b = 1.0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle ({self.a}, {self.b})'
    def perimetras(self):
        return 2*self.a + 2*self.b
    def plotas(self):
        return self.a*self.b


staciakampis = Staciakampis(3, 4)
print(staciakampis)
print(staciakampis.perimetras())
print(staciakampis.plotas())
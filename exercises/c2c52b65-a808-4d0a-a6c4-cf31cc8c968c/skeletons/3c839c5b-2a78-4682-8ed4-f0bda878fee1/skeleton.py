class Drabuziai:
    def __init__(u, medziaga, spalva):
        u.medziaga = medziaga
        u.spalva = spalva
    def aprasymas(u):
        return u.medziaga + ', kurios spalva: ' + u.spalva
class Striuke(Drabuziai):
    def aprasymas(u):
        return 'Striukė (' + Drabuziai.aprasymas(u) + ')'

striuke = Jacket('oda', 'juoda')
print(striuke.aprasymas())

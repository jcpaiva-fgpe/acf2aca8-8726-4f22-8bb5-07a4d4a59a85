class Drabuziai:
    def __init__(u, medziaga, spalva):
        u.medziaga = medziaga
        u.spalva = spalva
    def aprasymas(u):
        return u.medziaga + ', kurios spalva: ' + u.spalva
class Striuke(Drabuziai):
    def aprasymas(u):
        return 'Striukė (' + Drabuziai.aprasymas(u) + ')'
class Kelnes(Drabuziai):
    def aprasymas(u):
        return 'Kelnės (' + Drabuziai.description(u) + ')'

striuke = Striuke('oda', 'juoda')
print(striuke.aprasymas())
kelnes = Kelnes('džinsai', 'mėlyna')
print(triusikai.aprasymas())

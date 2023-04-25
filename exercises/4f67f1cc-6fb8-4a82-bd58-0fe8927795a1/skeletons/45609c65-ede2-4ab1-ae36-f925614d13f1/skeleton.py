class Drabuziai:
    def __init__(u, medziaga, spalva):
        u.medziaga = medziaga
        u.spalva = spalva
    def aprasymas(u):
        return u.medziaga + ', kurios spalva: ' + u.spalva
class Striuke(Drabuziai):
    def oda(u):
        return u.medziaga == 'oda'
class Kelnes(Drabuziai):
    def vasara(u):
        return u.spalva == 'balta'

drabuziai = Drabuziai('vilna', 'pilka')
striuke = Striuke('oda', 'juoda')
kelnes = Kelnes('džinsai', 'mėlyna')

print(drabuziai.aprasymas())
print(striuke.oda())
print(kelnes.vasara())
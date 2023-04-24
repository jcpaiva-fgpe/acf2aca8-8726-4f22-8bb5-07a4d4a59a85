class Queens:
    def __init__(self, dimension):
        self.dimension = dimension # šachmatų lentos matmenys (stulpelių skaičius)
        self.a = {i: True for i in range(1, dimension + 1)}
        # a[i] a[i] reiškia, kad i-oje eilutėje nėra karalienės
        self.b={i: True for i in range(2, 2 * dimension + 1)}
        # b[i] reiškia, kad i-oje įstrižainėje nėra karalienės /
        self.c={i: True for i in range(1 - dimension, dimension)}
        # c[i] reiškia, kad i-oje įstrižainėje nėra karalienės \
        self.x={ }
        # x[i] yra fiksuota karalienės padėtis i-ajame stulpelyje
    
    def set(self, i = 1): # i - stulpelio numeris
        for j in range(1, self.dimension + 1): # j - eilutės numeris
            if self.a[j] and self.b[i + j] and self.c[i - j]:
                self.x[i] = j # bandome uždėti ant [i, j]
                self.a[j] = self.b[i + j] = self.c[i - j] = False # pažymime, kad užimta
                if i == self.dimension: return True # tai buvo paskutinė karalienė
                if not self.set(i + 1): # nepavyko įdėti kitos karalienės
                    self.a[j] = self.b[i + j] = self.c[i - j] = True # pažymime laisvą
                else: return True 
        return False # nepavyko įdėti šios karalienės

    def __str__(self):
        rx = dict(zip(self.x.values(), self.x.keys()))
        s = ""
        for j in range(1, self.dimension + 1):
            s += '|' + '+|' * (rx[j] - 1) + 'H|' + '+|' * (self.dimension - rx[j]) + '\n'
        return s
    
checkerboard = Queens(8)
checkerboard.set()
print(str(checkerboard)[:-1])
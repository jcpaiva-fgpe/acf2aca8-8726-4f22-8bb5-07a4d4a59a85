class Sprendimas(object):
   def exist(self, matrica, zodis):
      n =len(matrica)
      m = len(matrica[0])
      for i in range(n):
         for j in range(m):
            if zodis[0] == matrica[i][j]:
               if self.find(matrica,zodis,i,j):
                  return True
      return False
   def find(self, matrica,zodis,eilute,stulpelis,i=0):
      if i== len(zodis):
         return True
      if eilute>= len(matrica) or eilute <0 or stulpelis >=len(matrica[0]) or stulpelis<0 or zodis[i]!=matrica[eilute][stulpelis]:
         return False
      matrica[eilute][stulpelis] = '*'
      rez = self.find(matrica,zodis,eilute+1,stulpelis,i+1) or self.find(matrica,zodis,eilute-1,stulpelis,i+1) or self.find(matrica,zodis,eilute,stulpelis+1,i+1) or self.find(matrica,zodis,eilute,stulpelis-1,i+1)
      matrica[eilute][stulpelis] = zodis[i]
      return rez
ob1 = Sprendimas()
print(ob1.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))

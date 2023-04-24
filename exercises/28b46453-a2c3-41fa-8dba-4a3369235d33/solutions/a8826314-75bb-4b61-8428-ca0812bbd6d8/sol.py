class Sprendimas(object):
   def minPathSum(self, tinklelis):
      eilute = len(tinklelis)-1
      stulpelis = len(tinklelis[0])-1
      i=eilute-1
      j=stulpelis-1
      while j>=0:
         tinklelis[eilute][j]+=tinklelis[eilute][j+1]
         j-=1
      while i>=0:
         tinklelis[i][stulpelis]+=tinklelis[i+1][stulpelis]
         i-=1
      j=stulpelis-1
      i = eilute-1
      while i>=0:
         while j>=0:
            tinklelis[i][j] += min(tinklelis[i][j+1],tinklelis[i+1][j])
            j-=1
         j=stulpelis-1
         i-=1
      return(tinklelis[0][0])
sp = Sprendimas()
print(sp.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

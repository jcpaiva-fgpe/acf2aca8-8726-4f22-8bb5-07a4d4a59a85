class Sprendimas(object):
   def arTeisingas(self, sudoku_matrica):
      """
      :type sudoku_matrica: List[List[str]]
      :rtype: bool
      """
      for i in range(9):
         eilute = {}
         stulpelis = {}
         blokas = {}
         eilute_kubas = 3 * (i//3)
         stulpelis_kubas = 3 * (i%3)
         for j in range(9):
          if sudoku_matrica[i][j]!='.' and sudoku_matrica[i][j] in eilute:
            return False
          eilute[sudoku_matrica[i][j]] = 1
          if sudoku_matrica[j][i]!='.' and sudoku_matrica[j][i] in stulpelis:
            return False
          stulpelis[sudoku_matrica[j][i]] = 1
          rc= eilute_kubas+j//3
          cc = stulpelis_kubas + j%3
          if sudoku_matrica[rc][cc] in blokas and sudoku_matrica[rc][cc]!='.':
            return False
          blokas[sudoku_matrica[rc][cc]]=1
      return True
sp = Sprendimas()
teisingas = sp.arTeisingas([
   ["5","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]])
if teisingas:
    print("Sudoku teisingas")

def knight(dimension, x = 0, y = 0):
    def jump (movement, x, y):
        nonlocal dx, dy, sz
        for k in range(8):
            xn = x + dx[k]
            yn = y + dy[k]
            if (xn in range(dimension)) and (yn in range(dimension)):
               if sz[xn][yn] == 0:
                  sz[xn][yn] = movement
                  if movement == dimension * dimension: 
                      return True
                  if jump(movement + 1, xn, yn): 
                      return True 
                  sz[xn][yn] = 0 
        return False
    
    dx = ( 1,  2, 2, 1, -1, -2, -2, -1) 
    dy = (-2, -1, 1, 2,  2,  1, -1, -2) 
    sz = [ [0 for x in range(dimension)] for y in range(dimension) ] 
    sz[x][y] = 1 
    if not jump(2, x, y): 
        print("Failed.")
    else: 
        for y in range(dimension): 
            print('|', end='')
            for x in range(dimension):
                print(f"{sz[x][y]:2}", end="|")
            print()

d = int(input())
knight(d)
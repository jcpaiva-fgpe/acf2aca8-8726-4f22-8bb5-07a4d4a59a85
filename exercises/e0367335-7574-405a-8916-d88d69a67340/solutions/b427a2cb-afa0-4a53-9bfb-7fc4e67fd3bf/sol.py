def n_didziausias(li, b):
    if b < 1 or b > len(li): 
        return f"Antrasis funkcijos parametras: {b} yra neteisingas."
    li.sort()
    
    def didziausias(): 
        return li[-1]
    if b == 1: return didziausias()
    li.remove(didziausias())
    return(n_didziausias(li, b-1))

#############################################
# TEST DATA ### DON'T TOUCH THIS.           #
# ----------------------------------------- #
print(n_didziausias(input().split(), int(input())))   #
#############################################

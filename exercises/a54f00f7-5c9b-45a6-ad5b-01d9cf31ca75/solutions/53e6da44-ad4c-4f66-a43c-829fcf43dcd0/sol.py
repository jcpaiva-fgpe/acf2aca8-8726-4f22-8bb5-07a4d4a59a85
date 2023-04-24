def nulinti():
    global taskai
    taskai = 0

def didinti():
    global taskai
    taskai +=1

nulinti(); didinti(); didinti(); print(taskai)
nulinti(); print(taskai)

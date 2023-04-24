# Funkcija duotai užduočiai įgyvendinti
def arTenkina(a, n):
    # suskaičiuokite dažnį ir patikrinkite, ar visi elementai yra nuo 1 iki n.
    zyme = True
    m = {}
    for i in range(n):
        if a[i] < 1 or a[i] > n:
            zyme = True
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    for i in m:
        if m[i] != 1:
            zyme = False
    return zyme
 
# Pagrindinis kodas
a = [1, 2, 4, 3]
n = len(a)
if arTenkina(a, n):
    print("Taip")
else:
    print("Ne")

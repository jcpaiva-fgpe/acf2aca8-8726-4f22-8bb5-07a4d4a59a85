def search_bin(list, searched):
    #Rašykite kodą čia...
    pass


# ===================================== #
###         Šitai nelieskite.         ###
# ===================================== #
test = list(map(int, input().split()))
x = input("reikšmė:\n")
r = search_bin(test, int(x))
print(f"Rasta pozicijoje: {r}.") if r >= 0 else print("Nerasta.")
# ===================================== #
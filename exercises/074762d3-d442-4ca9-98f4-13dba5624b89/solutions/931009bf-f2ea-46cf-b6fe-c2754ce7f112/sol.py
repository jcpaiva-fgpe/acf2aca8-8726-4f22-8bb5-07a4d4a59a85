def search_bin(list, searched):
    left = 0
    right = len(list)
    while left <= right: 
        mid = (left + right) // 2
        middle = list[mid]
        if middle == searched: return mid
        if middle > searched: right = mid - 1
        else: left = mid + 1
    return -1

test = list(map(int, input().split()))
x = input("reikšmė:\n")
r = search_bin(test, int(x))
print(f"Rasta pozicijoje: {r}.") if r >= 0 else print("Nerasta.")
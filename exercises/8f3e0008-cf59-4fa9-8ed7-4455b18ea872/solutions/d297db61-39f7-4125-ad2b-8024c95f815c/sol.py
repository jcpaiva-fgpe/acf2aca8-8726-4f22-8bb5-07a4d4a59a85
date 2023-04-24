def qsort(list_a):
    if len(list_a) <= 1:
        return list_a
    else:
        middle = list_a[len(list_a) // 2]
        smaller = qsort([x for x in list_a if x < middle])
        higher = qsort([x for x in list_a if x > middle])
        the_same = [x for x in list_a if x == middle]
        return smaller + the_same + higher

test = list(map(int, input().split()))
print("List:", test)
print("Sorted:", qsort(test))

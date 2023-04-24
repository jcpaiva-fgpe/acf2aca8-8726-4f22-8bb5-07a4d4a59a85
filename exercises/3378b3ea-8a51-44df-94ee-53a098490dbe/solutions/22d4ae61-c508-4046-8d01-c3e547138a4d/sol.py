def change(ret):
    denominations = [.01, .02, .05, .1, .2, .5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    fl = -0.01
    for d in denominations:
        if d == ret: return d
        elif d < ret: fl = d
    temp = round(ret - fl, 2)
    if fl<0: return 0 
    return ' Euro, '.join([f'{fl}', f'{change(temp)}'])

cash, bill = map(float, input().split()) # (200. 171.24)
r = round(cash - bill, 2)
print(f'({r = } Euro)', change(r), end=' Euro\n')

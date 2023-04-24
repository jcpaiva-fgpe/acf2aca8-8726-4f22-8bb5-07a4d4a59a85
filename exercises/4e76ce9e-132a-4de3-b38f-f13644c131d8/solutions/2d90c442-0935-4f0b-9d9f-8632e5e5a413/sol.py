def kvadratine_lygtis(a, b, c):
    delta = b**2 - 4*a*c
    if delta == 0:
        return -b/2*a

    elif delta > 0:
        x1 = (-b - delta**0.5)/2*a
        x2 = (-b + delta**0.5)/2*a
        return x1, x2
    else: return


# ------------------------------------ #
#     Nekeiskite šio kodo              | 
# ------------------------------------ #
try:
    print(kvadratine_lygtis(*map(int, input().split())))  
except:
    print(kvadratine_lygtis(-1,2,3))                  
    print(kvadratine_lygtis(1,2,1))                   
    print(kvadratine_lygtis(2,1,1))    
# ------------------------------------- #
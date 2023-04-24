# Funkcija, kuri skaičiuoja, kiek būdų nudažyti lentas
def dazymo_budai(n, k):
     
    dp = [0] * (n + 1)
    viso = k
    modulis = 1000000007
     
    dp[1] = k
    dp[2] = k * k   
     
    for i in range(3,n+1):
        dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % modulis
         
    return dp[n]
   
# Iškvietimas, kai n = 3 ir k = 2
n = 3
k = 2
print(dazymo_budai(n, k))

print('Darbo sutarčių skaičius:') 
employment_contracts = int(input()) # Tik sveiki skaičiai
    
print('Kompiuteris? True ar False?')
commuter = input()

costs = 0
if employment_contracts == 1: 
    costs = 3600 if commuter == "True" else 3000
elif employment_contracts > 1: 
    costs = 5400 if commuter == "True" else 4500
else: costs = costs

print('Metinės pajamų sąnaudos yra', costs, 'eurų.')
salys = set()
salis = '?'

while (True):
    print('Šalies pavadinimas?')
    salis = input()
    
    if not salis: break # Test issue.
    if salis in salys:
    	print(False)
        
    else: salys.add(salis)
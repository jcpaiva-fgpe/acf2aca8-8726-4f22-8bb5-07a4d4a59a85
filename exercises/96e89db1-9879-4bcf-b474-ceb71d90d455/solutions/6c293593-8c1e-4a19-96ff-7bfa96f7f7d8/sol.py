telefonai = {'policija': 114, 'ugniagesiai': 113, 'greitoji pagalba': 112}

for k, v in telefonai.copy().items(): 
    if v % 3 == 0: 
       print(k)
       telefonai.pop(k)
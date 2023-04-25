telefonai = {'policija': 114, 'ugniagesiai': 113, 'greitoji pagalba': 112}
telefonai = dict(zip(telefonai.values(), telefonai.keys())) 
#telefonai = {v: k for k, v in telefonai.items()}
print(telefonai)
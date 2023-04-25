telefonai = {'policija': 114, 'ugniagesiai': 113, 'greitoji pagalba': 112}
for k, v in telefonai.items():
    print(k + str(v).rjust(24 - len(k), '.'))
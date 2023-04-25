telefonai = {'policija': 114, 'ugniagesiai': 113, 'greitoji pagalba': 112}
inp = input()
if not inp in telefonai.keys(): print("Nėra!")
else: print(telefonai[inp])
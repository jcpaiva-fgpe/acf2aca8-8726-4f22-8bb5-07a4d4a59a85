print('Eilutė?')
txt = input()
if txt.count('(') + txt.count(')') == 2:
    txt = txt[:txt.find('(')+1] + txt[txt.rfind(')'):]
print(txt)
zodziai = {'diena': 'day', 'naktis': 'night', 'vasara': 'summer', 'pavasaris': 'spring'}

while True:
    zodis = input("Žodis:")
    if not zodis: break
    elif(zodis not in zodziai.keys()): msg = "Nėra!"
    else: msg = zodziai[zodis]
    print(msg)

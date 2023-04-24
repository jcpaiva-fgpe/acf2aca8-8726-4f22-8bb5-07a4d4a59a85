neteisingai = 0

while neteisingai < 3:
    print('Kodas?')
    kodas = input()

    if kodas == 'Valio!':
        print('Teisingai!')
        break
    else:
        neteisingai +=1
        if neteisingai == 3:
            print('Neteisingai!') 
            break

        print(False)
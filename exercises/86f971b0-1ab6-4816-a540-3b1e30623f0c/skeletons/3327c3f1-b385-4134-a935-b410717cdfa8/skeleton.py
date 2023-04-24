rinkinys = set(('Mauglis. Dalis I', 'Mauglis. Dalis II', 'Tomas ir Džeris. Dalis I',  'Tomas ir Džeris. Dalis II' ))
mauglis = set(('Mauglis. Dalis I', 'Mauglis. Dalis II', 'Mauglis. Dalis III' ))
tomas_dzeris = set(('Tomas ir Džeris. Dalis I',  'Tomas ir Džeris. Dalis II' ))
print('Esi laimingasis, kuris turi Tomo ir Džerio seriją:')
for t in tomas_dzeris.union(rinkinys):
    print(t)
if rinkinys >= mauglis:
    print('Turi pilną Mauglio seriją.')
else:
    print ('Trūksta šių Mauglio dalių:')
    for t in mauglis.symmetric_difference(rinkinys):
        print(t)
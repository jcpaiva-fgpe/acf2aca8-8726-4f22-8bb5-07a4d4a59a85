#Funkcijos sena_data() pavyzdys
def senovine_data(d):
    def month():
        return ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'][int(d[1])-1]
    d = d.split('-')
    return d[2]+'.'+month()+'.'+d[0]
#print(senovine_data('2019-11-24'))

#Jūsų funkcija
def n_didziausias():
    
    pass
#print(bli([3,6,8,1,4], 3))

#############################################
# Testavimo duomenys ### Nelieskite.        #
# ----------------------------------------- #
print(bli(input().split(), int(input())))   #
#############################################


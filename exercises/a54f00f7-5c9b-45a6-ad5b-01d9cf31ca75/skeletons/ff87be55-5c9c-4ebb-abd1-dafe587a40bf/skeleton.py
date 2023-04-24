#Funkcijos registruoti() pavyzdys
def registruoti(entry):
    global log
    log += [entry]

log = []    
registruoti("Gavau 10. Puiku.")
registruoti("Gavau 4. Blogai.")
registruoti("Gavau 7. Šiaip sau.")
print('\n'.join(log))




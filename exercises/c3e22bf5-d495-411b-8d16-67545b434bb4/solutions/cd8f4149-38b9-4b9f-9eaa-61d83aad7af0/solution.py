def check_in(guest):

    I = ['LARRY', 'MEGAN', 'CONSUL', 'NOTARY', 'GOBLIN', 'CIRO']
    U = ['VAMPIRE' 'SKELETON', 'DRAKE', 'VOLDEMORT']
    
    if guest in I:
        return "OK"
    elif guest in U:
        return "CALL GUARDS!"
    else:
        return "NOT IN LIST"



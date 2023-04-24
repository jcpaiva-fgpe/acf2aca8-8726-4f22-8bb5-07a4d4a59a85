simboliai = set(('!','@','#','$','%','^','&'))
simboliai.discard('$')

if '$' in simboliai:
    print (u'$ ženklas vis dar yra!')
else:
    print (u'Pagaliau! $ ženklas dingo.')

s = input()
msg = {}
for i in s.split():
    msg.setdefault(i, 0) 
    msg.update({i: msg[i] + 1})
print(msg)
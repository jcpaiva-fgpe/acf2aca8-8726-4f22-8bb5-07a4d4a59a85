t = ['Introduction', 'Chase', 'Who is the bearded man', 'The Devil at midnight', 'Behind the closet']
p = [5, 12, 17, 20, 24]
for i in range(len(list(zip(t, p)))):
    print(t[i], "", sep = str(p[i]).rjust(40 - len(t[i]), '.'))
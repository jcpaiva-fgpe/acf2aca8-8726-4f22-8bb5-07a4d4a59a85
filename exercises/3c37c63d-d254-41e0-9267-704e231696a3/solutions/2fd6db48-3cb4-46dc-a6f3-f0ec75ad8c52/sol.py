print("String?")
txt = input()

txt = max(txt.split(), key = len)
print("Output:", txt)
class Kvadratas: 
   krastine = 1.0
   def __init__(f, krastine):
        f.krastine = krastine
   def perimetras(f):
       return f.krastine * 4.0
       
kvadratas = Kvadratas(3.0)
print(kvadratas.perimetras())
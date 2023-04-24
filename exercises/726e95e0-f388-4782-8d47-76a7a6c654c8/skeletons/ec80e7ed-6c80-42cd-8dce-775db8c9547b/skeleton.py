def fib(n):
   if n < 2:
      return n
   else:
      return fib(n - 1) + fib(n - 2)

n = int(input("n:\n"))
print(f'{fib(n) = }')
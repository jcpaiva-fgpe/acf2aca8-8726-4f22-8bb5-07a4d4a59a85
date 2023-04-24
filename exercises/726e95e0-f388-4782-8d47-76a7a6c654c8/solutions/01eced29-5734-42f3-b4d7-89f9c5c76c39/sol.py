class Memo():
    calculated = {0: 0, 1: 1}
    @classmethod
    def fib(cls, n):
        if n not in cls.calculated:
            cls.calculated[n] = cls.fib(n - 1) + cls.fib(n - 2)
        return cls.calculated[n]

n = int(input("n:\n"))
print(f"fib({n}) =", Memo.fib(n))
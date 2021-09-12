from functools import lru_cache

@lru_cache()
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

for i in range(1, 1000):
    print(i, ":", fib(i))





def fib(n):
    base = [0, 1]
    for i in range(2, n + 1):
        base.append(base[i - 2] + base[i - 1])

    return base[n]


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(5))

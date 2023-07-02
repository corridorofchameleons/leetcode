import time


def time_deco(func):
    def wrapper():
        st = time.time()
        result = func()
        en = time.time()
        total = en - st
        print(f'total time: {total:.6f}')
        return result
    return wrapper


def cache_deco(func):
    fibs = {}

    def wrapper(n):
        if n in fibs:
            return fibs[n]
        else:
            fibs[n] = func(n)
            return func(n)
    return wrapper


@cache_deco
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


@time_deco
def main():
    print(fib(950))


if __name__ == '__main__':
    main()

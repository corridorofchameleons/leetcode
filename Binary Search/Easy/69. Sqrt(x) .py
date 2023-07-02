def mySqrt(x):
    if x == 0 or x == 1:
        return x
    start = 0
    end = x
    while start < end - 1:
        n = (end + start) // 2
        if n * n == x:
            return n
        elif n * n > x:
            end = n
        else:
            start = n
    return start


x = 198
print(mySqrt(x))
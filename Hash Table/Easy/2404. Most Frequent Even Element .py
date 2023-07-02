def mostFrequentEven(nums):
    d = {num: 0 for num in nums if num % 2 == 0}

    if not d:
        return -1

    for num in nums:
        if num % 2:
            continue
        d[num] += 1

    f = 0
    for i in d.values():
        if i > f:
            f = i

    result = []
    for num in d:
        if d[num] == f:
            result.append(num)

    return min(result)


print(mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
print(mostFrequentEven([4, 4, 4, 9, 2, 4]))
print(mostFrequentEven([]))
print(mostFrequentEven([1, 5, 3]))
print(mostFrequentEven([3, 4, 6, 2, 3, 2, 4, 7]))

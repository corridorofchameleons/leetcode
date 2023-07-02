def largP(nums):
    result = 0
    sides = sorted(nums)
    for i in range(len(sides) - 2):
        if sides[i] + sides[i + 1] > sides[i + 2] and sides[i] + sides[i + 1] + sides[i + 2] > result:
            result = sides[i] + sides[i + 1] + sides[i + 2]
    return result


print(largP([2, 1, 2]))
print(largP([1, 2, 1, 10]))

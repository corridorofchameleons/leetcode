def smallerNums(nums):
    result = []
    d = {}
    tnums = sorted(nums)
    for i in range(len(tnums)):
        if tnums[i] not in d:
            d[tnums[i]] = i
    for n in nums:
        result.append(d[n])
    return result


print(smallerNums([8, 1, 2, 2, 3]))
print(smallerNums([6, 5, 4, 8]))
print(smallerNums([7, 7, 7, 7]))

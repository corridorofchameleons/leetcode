from collections import OrderedDict


def fMP(nums):
    n_max = max(nums)
    d = OrderedDict()
    d.update({n: False for n in range(1, len(nums) + 1)})
    for n in nums:
        if n in d:
            d[n] = True
    for el in d:
        if not d[el]:
            return el
    return n_max + 1


print(fMP([1, 2, 0]))
print(fMP([3, 4, -1, 1]))
print(fMP([7, 8, 9, 11, 12]))
print(fMP([1, 2, -4, 3, 5, 4, -6]))

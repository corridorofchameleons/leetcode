def sn(nums):
    ns = {}
    for num in nums:
        if num in ns:
            ns[num] = False
        else:
            ns[num] = True
    for n in ns:
        if ns[n]:
            return n


print(sn([4, 1, 2, 1, 2, 1, 2]))
print(sn([0, 1, 0, 1, 0, 1, 99]))
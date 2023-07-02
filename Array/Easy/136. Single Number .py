def sn(nums):
    ns = set()
    for num in nums:
        if num in ns:
            ns.remove(num)
        else:
            ns.add(num)
    return ns.pop()


print(sn([4, 1, 2, 1, 2]))
print(sn([1]))

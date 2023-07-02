def three_sum(nums):
    result = set()

    def two_sum(ns, k):
        s = set()
        for n in ns:
            if -n in s:
                l = sorted([k, n, -(k + n)])
                l = tuple(l)
                if l not in result:
                    result.add(l)
            s.add(n + k)

    for i in range(len(nums) - 2):
        two_sum(nums[i + 1:], nums[i])

    return list(result)


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0]))
print(three_sum([0, 1, 1]))

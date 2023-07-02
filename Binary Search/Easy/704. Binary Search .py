def search(nums, target):
    tnums = nums

    def int_search(tnums):
        if len(tnums):
            i = len(tnums) // 2
            if tnums[i] == target:
                return nums.index(tnums[i])
            elif tnums[i] > target:
                return int_search(tnums[:i])
            else:
                return int_search(tnums[i + 1:])
        else:
            return -1

    return int_search(tnums)


nums = [-2, 0, 5, 14, 17, 20, 31, 42, 53, 61, 69, 72, 99]
nums_2 = []
nums_3 = [1]
print(search(nums, 72))
print(search(nums, 0))
print(search(nums, 73))
print(search(nums_2, 73))
print(search(nums_3, 1))

def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        else:
            d[num] = i


nums = [3, 3]
target = 6


print(twoSum(nums, target))



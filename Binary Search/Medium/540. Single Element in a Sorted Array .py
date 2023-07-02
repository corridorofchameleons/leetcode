def singleNotD(nums):
    start = 0
    end = len(nums)
    while start < end - 1:
        n = (start + end) // 2
        if n < len(nums) - 1 and nums[n] == nums[n + 1]:
            if n % 2:
                end = n
            else:
                start = n
        elif nums[n] == nums[n - 1]:
            if n % 2:
                start = n
            else:
                end = n
        else:
            return nums[n]
    return nums[start]


print(singleNotD([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(singleNotD([3, 3, 7, 7, 10, 11, 11]))
print(singleNotD([3, 3, 7, 7, 10, 10, 11]))
print(singleNotD([1, 3, 3, 7, 7, 10, 10, 11, 11]))

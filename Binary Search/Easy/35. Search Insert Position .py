def searchIns(nums, target):
    if target > nums[-1]:
        return len(nums)
    if target <= nums[0]:
        return 0

    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            if len(nums[start: end]) == 1:
                return mid
            end = mid
        if nums[mid] < target:
            if len(nums[start: end]) == 1:
                return mid + 1
            start = mid


print(searchIns([1, 3, 5, 6], 5))
print(searchIns([1, 3, 5, 6], 2))
print(searchIns([1, 3, 5, 6], 7))
print(searchIns([1, 3, 5, 6], 0))
print(searchIns([1], 1))
print(searchIns([1, 3, 5], 4))

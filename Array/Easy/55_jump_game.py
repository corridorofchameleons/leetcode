def permute(nums):
    result = []
    for i in range(len(nums)):
        t_nums = nums.copy()
        n_nums = [t_nums.pop(i)]
        for j in range(1, 3):
            k_nums = n_nums.copy()
            n_nums.append(nums[j])


        print(n_nums)
        print(t_nums)

print(permute([1, 2, 3]))

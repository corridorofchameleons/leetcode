def rearrangeArray(nums):
    pos_list = []
    neg_list = []
    result = []
    for n in nums:
        if n > 0:
            pos_list.append(n)
        else:
            neg_list.append(n)

    for i in range(len(pos_list)):
        result.append(pos_list[i])
        result.append(neg_list[i])

    return result


print(rearrangeArray([3, 1, -2, -5, 2, -4]))
print(rearrangeArray([-1, 1]))
print(rearrangeArray([-3, -1, -2, 5, 2, 4]))
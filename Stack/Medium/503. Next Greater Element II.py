def nextGreaterElements(nums):
    t_nums = nums * 2
    result = []
    ln = len(nums)
    for i in range(ln):
        st = [-1]
        for j in range(i, i + ln):
            if t_nums[j] > nums[i]:
                st.append(t_nums[j])
                break
        result.append(st.pop())

    return result
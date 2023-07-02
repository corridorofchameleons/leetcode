def balanced_string(s):
    result = 0
    cnt_r = 0
    cnt_l = 0
    for i in range(len(s)):
        if s[i] == 'R':
            cnt_r += 1
        if s[i] == 'L':
            cnt_l += 1
        if cnt_l == cnt_r:
            result += 1
            cnt_r, cnt_l = 0, 0

    return result


print(balanced_string('LR'))
print(balanced_string('LRLR'))
print(balanced_string('LLRRLLLRLRRR'))
print(balanced_string('RLRRLRLLRRLLRRLL'))

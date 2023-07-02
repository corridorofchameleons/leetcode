def reverseVowels(s):
    result = ''
    vows = {'a', 'o', 'u', 'i', 'e'}
    s_l = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        while left < len(s_l) and s_l[left].lower() not in vows:
            left += 1
        while right >= 0 and s_l[right].lower() not in vows:
            right -= 1
        if left < right:
            s_l[left], s_l[right] = s_l[right], s_l[left]
            left += 1
            right -= 1

    for sym in s_l:
        result += sym

    return result


print(reverseVowels('banumnomip'))
print(reverseVowels('abbu'))
print(reverseVowels('Annotate'))
print(reverseVowels('Idiots'))
print(reverseVowels(''))
print(reverseVowels('G'))
print(reverseVowels('.,'))

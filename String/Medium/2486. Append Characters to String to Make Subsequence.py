def appendCharacters(s, t):
    c_s = 0
    c_t = 0
    while c_s < len(s) and c_t < len(t):
        while s[c_s] != t[c_t]:
            if c_s < len(s) - 1:
                c_s += 1
            else:
                return len(t[c_t:])
        c_s += 1
        if c_s >= len(s):
            return len(t[(c_t + 1):])
        if c_t < len(t) - 1:
            c_t += 1
        else:
            return 0
    return len(t[c_t:])


print(appendCharacters('abcd', 'abc'))
print(appendCharacters('abcd', 'abcde'))
print(appendCharacters('anbncnd', 'abcde'))
print(appendCharacters('anbncnd', 'abcd'))
print(appendCharacters('z', 'abcde'))
print(appendCharacters('z', ''))
print(appendCharacters('', ''))
print(appendCharacters('', 'zz'))

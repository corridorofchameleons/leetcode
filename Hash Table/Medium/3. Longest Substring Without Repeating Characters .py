def ls(s):
    ans = 0
    for i in range(len(s)):
        j = i
        syms = set()
        for j in range(j, len(s)):
            if s[j] in syms:
                break
            syms.add(s[j])
            j += 1
        if j - i > ans:
            ans = j - i

    return ans


print(ls("abcabcbb"))
print(ls("bbbbb"))
print(ls("pwwkew"))
print(ls(""))
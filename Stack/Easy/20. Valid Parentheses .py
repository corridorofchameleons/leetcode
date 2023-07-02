def isValid(s):
    parens = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    st = []
    for p in s:
        if st and p in parens and parens[p] == st[-1]:
            st.pop()
        else:
            st.append(p)

    return False if st else True


print(isValid("([]())[]"))
print(isValid("(]"))
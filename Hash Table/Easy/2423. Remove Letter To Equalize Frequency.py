def eq_freq(word):
    d = {sym: word.count(sym) for sym in word}
    freqs = [f for f in d.values()]
    d2 = {f: 0 for f in freqs}
    for f in freqs:
        d2[f] += 1

    l = []
    for k, v in d2.items():
        l.append([k, v])
    l.sort()

    if len(l) == 1 and (l[0][0] == 1 or l[0][1] == 1):
        return True

    elif len(l) == 2:
        if l[0][0] == 1 and l[0][1] == 1:
            return True
        elif l[1][0] - l[0][0] == 1 and l[1][1] == 1:
            return True

    return False


# print(eq_freq('abcc'))
# print(eq_freq('aazz'))
# print(eq_freq('abbcc'))
# print(eq_freq('bac'))
# print(eq_freq('ddaccb'))
# print(eq_freq('zz'))
print(eq_freq("babbdd"))

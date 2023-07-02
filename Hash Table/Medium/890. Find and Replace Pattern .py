def farp(words, pattern):
    def get_pat(s: str):
        pat = {sym: [] for sym in s}
        for i, sym in enumerate(s):
            pat[sym].append(i)

        return tuple(pat.values())

    result = []

    for word in words:
        if get_pat(word) == get_pat(pattern):
            result.append(word)

    return result


print(farp(["abc", "deq", "mee", "aqq", "dkd", "ccc"], 'abb'))
print(farp(["a", "b", "c"], 'a'))

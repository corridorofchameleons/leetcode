def count_substr(s):
    if not s:
        return 0
    result = 0
    for j in range(len(s)):
        if s[:j + 1] == s[j::-1]:
            print(s[:j + 1], s[j::-1])
            j += 1
            result += 1

    for i in range(1, len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] == s[j:i - 1:-1]:
                print(s[i:j + 1], s[j:i - 1:-1])
                j += 1
                result += 1

    return result


# print(count_substr('12234'))
# print(count_substr('1223432'))
print(count_substr('baaa'))
# print(count_substr(''))

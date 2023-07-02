from collections import Counter


def freq_sort(s):
    result = ''
    cntr = Counter(s)
    for a in cntr.most_common():
        for i in range(a[1]):
            result += a[0]
    return result


print(freq_sort('tree'))
print(freq_sort('cccaaa'))
print(freq_sort(''))
print(freq_sort('aabaccacccAt'))

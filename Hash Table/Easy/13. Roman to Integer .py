def romantoint(s):
    enigma = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    for i in range(0, len(s)):
        if i == len(s) - 1 or enigma[s[i]] >= enigma[s[i + 1]]:
            result += enigma[s[i]]
        else:
            result -= enigma[s[i]]

    return result if result else None


print(romantoint('XVIII'))
print(romantoint('XIX'))
print(romantoint('I'))
print(romantoint('MCMXCIV'))


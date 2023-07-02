def validPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:

        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            str1 = s[left + 1:right + 1]
            str2 = s[left:right]
            if str1 == str1[::-1] or str2 == str2[::-1]:
                return True
            else:
                return False
            break

    return True


print(validPalindrome('aba'))
print(validPalindrome('abca'))
print(validPalindrome('abc'))
print(validPalindrome(''))
print(validPalindrome('abba'))
print(validPalindrome('abcbac'))
print(validPalindrome("mlcuppuculm"))
print(validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))

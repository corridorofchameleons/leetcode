from collections import Counter

def can(ransomNote, magazine):
    syms = Counter(magazine)
    for a in ransomNote:
        if a not in syms or syms[a] == 0:
            return False
        else:
            syms[a] -= 1
    return True

print(can('aacbn', 'aacbnn'))
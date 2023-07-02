from collections import Counter
def shortestCompletingWord(licensePlate, words) -> str:
    sym_set = {x: licensePlate.lower().count(x) for x in licensePlate.lower() if not x.isdigit() and x != ' '}

    def no_left(syms):
        for sym in syms:
            if syms[sym] > 0:
                return False
        return True

    for word in sorted(words, key=len):
        t_syms = sym_set.copy()
        for s in word:
            if s in t_syms:
                t_syms[s] -= 1
        if no_left(t_syms):
            return word



licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(shortestCompletingWord(licensePlate, words))

licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print(shortestCompletingWord(licensePlate, words))

licensePlate = "Ah71752"
words = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]
print(shortestCompletingWord(licensePlate, words))



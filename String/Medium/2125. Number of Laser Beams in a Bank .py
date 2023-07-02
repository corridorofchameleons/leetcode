def numberOfBeams(bank):
    count = 0
    sums = []
    for i in range(len(bank)):
        a = [int(sym) for sym in bank[i]]
        if sum(a):
            sums.append(sum(a))
    for i in range(len(sums)):
        if i < len(sums) - 1:
            count += sums[i] * sums[i + 1]

    return count


print(numberOfBeams(["011001", "000000", "010100", "001000"]))
print(numberOfBeams(["000", "111", "000"]))
print(numberOfBeams(["0001", "1110", "1000"]))


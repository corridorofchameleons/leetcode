def generate(numRows):
    result = [[1]]

    for i in range(1, numRows):
        tmp = [1] * (i + 1)
        for j in range(1, len(tmp) - 1):
            tmp[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(tmp)

    return result


print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(5))
print(generate(30))

def relativeS(arr1, arr2):
    result = []
    for a2 in arr2:
        for i in range(len(arr1)):
            if arr1[i] == a2:
                result.append(arr1[i])
                arr1[i] = None
    tarr = [a for a in arr1 if a != None]
    result += sorted(tarr)
    return result


print(relativeS([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
print(relativeS([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
print(relativeS([2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31], [2, 42, 38, 0, 43, 21]))

def sortTS(score, k):
    score.sort(key=lambda arr: arr[k], reverse=True)
    return score


print(sortTS([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2))
print(sortTS([[3, 4], [5, 6]], 0))

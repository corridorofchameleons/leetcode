def maxIC(costs, coins):
    costs.sort()
    left = coins
    result = 0
    while left > 0:
        for i in range(len(costs)):
            if costs[i] <= left:
                result += 1
                left -= costs[i]
            else:
                break
        break
    return result


print(maxIC([1, 3, 2, 4, 1], 7))
print(maxIC([10, 6, 8, 7, 7, 8], 5))
print(maxIC([1, 6, 3, 1, 2, 5], 20))

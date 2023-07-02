from collections import deque


def timereq(tickets, k):
    line = deque(tickets)
    result = 0
    while tickets[k] > 0:
        if line[0]:
            line[0] -= 1
        result += 1
        if line[0] == 0 and line[k] is line[0]:
            return result
        elif line[0] == 0:
            line.popleft()
        else:
            line.rotate(-1)
        k = k - 1 if k > 0 else len(line) - 1


print(timereq([2, 3, 2], 2))
print(timereq([5, 1, 1, 1], 0))


# line = deque()
# for i in range(1, 5):
#     line.append(i)
#
# print(line[1])
# line.rotate(-1)
# print(line[1])
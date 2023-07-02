from collections import deque


def findTW(n, k):
    circle = deque(range(1, n + 1))
    while len(circle) > 1:
        circle.rotate(-k + 1)
        circle.popleft()
    return circle[0]


print(findTW(5, 2))
print(findTW(6, 5))
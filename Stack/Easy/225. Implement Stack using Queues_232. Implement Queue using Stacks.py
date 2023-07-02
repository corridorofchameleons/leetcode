class MyStack:

    def __init__(self):
        self.st_1 = []  # don't need the second one if using an insert function
        # self.st_2 = []

    def push(self, x: int) -> None:
        self.st_1.insert(0, x)

        # self.st_2 = self.st_1.copy()
        # self.st_1.clear()
        # self.st_1.append(x)
        # self.st_1 += self.st_2
        # self.st_2 = []

    def pop(self) -> int:
        if not self.st_1:
            return None
        output = self.st_1[0]
        del self.st_1[0]
        return output

    def top(self) -> int:
        return self.st_1[0] if self.st_1 else None

    def empty(self) -> bool:
        return not self.st_1


class MyQueue:

    def __init__(self):
        self.st_1 = []
        self.st_2 = []

    def push(self, x: int) -> None:
        self.st_1.append(x)

    def pop(self) -> int:
        while self.st_1:
            self.st_2.append(self.st_1.pop())
        output = self.st_2.pop()
        while self.st_2:
            self.st_1.append(self.st_2.pop())
        return output

    def peek(self) -> int:
        while self.st_1:
            self.st_2.append(self.st_1.pop())
        output = self.st_2[-1]
        while self.st_2:
            self.st_1.append(self.st_2.pop())
        return output

    def empty(self) -> bool:
        return not self.st_1


# ms = MyStack()
# for i in range(1, 11):
#     ms.push(i)
#
# print(ms.st_1)
# print(ms.pop())
# print(ms.st_1)
# print(ms.top())
# print(ms.empty())


# mq = MyQueue()
# for i in range(1, 11):
#     mq.push(i)
#
# print(mq.st_1)
# print(mq.pop())
# print(mq.st_1)
# print(mq.peek())
# print(mq.empty())

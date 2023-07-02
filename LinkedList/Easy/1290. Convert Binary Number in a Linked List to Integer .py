class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        pows = []
        vals = []
        cur = head
        cnt = 0
        while cur:
            pows.append(cnt)
            vals.append(cur.val)
            cnt += 1
            cur = cur.next

        pows.reverse()
        for i in range(len(vals)):
            result += vals[i] * 2 ** pows[i]

        return result
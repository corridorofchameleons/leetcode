class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []

        def aaa(root, result):
            if root:
                if low <= root.val <= high:
                    result.append(root.val)
                aaa(root.left, result)
                aaa(root.right, result)

            return sum(result)

        return aaa(root, result)
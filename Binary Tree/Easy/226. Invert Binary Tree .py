class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def aaa(root):
            if root:
                if root.left or root.right:
                    root.left, root.right = root.right, root.left

                aaa(root.left)
                aaa(root.right)

        aaa(root)
        return root
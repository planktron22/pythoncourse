class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def _dfs(root, sum):
            if not root:
                return 0
            sum = sum * 10 + root.val
            if root.left == None and root.right == None:
                return sum
            return _dfs(root.left, sum) + _dfs(root.right, sum)

        return _dfs(root, 0)
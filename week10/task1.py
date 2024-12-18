class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        final = []
        path = []
        s = 0

        self.traverse(root, s, path, targetSum, final)
        return final

    def traverse(self, root, s, path, target, final):
        if root is not None:
            s += root.val
            path.append(root.val)
            if s == target and root.left is None and root.right is None:
                final.append(path[:])
            self.traverse(root.left, s, path, target, final)
            self.traverse(root.right, s, path, target, final)
            path.pop()
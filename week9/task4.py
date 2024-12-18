class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTree(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                for leftTree in generateTree(left, i - 1):
                    for rightTree in generateTree(i + 1, right):
                        root = TreeNode(i, leftTree, rightTree)
                        res.append(root)
            return res

        return generateTree(1, n)
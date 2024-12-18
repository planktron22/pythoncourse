class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def dfs(node):
            if node is None:
                return None
            left_right_most = dfs(node.left)
            right_right_most = dfs(node.right)
            if node.left:
                old_node_right = node.right
                node.left, node.right = None, node.left
                if left_right_most:
                    left_right_most.right = old_node_right

            if right_right_most:
                return right_right_most
            elif left_right_most:
                return left_right_most
            return node

        dfs(root)
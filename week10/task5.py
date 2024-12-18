class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths_from_node(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val == target:
                count += 1

            count += count_paths_from_node(node.left, target - node.val)
            count += count_paths_from_node(node.right, target - node.val)

            return count

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            count = count_paths_from_node(node, targetSum)

            count += dfs(node.left)
            count += dfs(node.right)

            return count

        return dfs(root)
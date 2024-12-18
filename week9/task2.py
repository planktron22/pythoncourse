class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0))
        visited = []

        while queue:
            node, level = queue.popleft()

            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

                try:
                    visited[level].append(node.val)
                except:
                    visited.append([node.val])

        return visited
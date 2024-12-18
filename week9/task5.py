class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = middle = last = prev = None
        cur = root
        while cur:
            if not cur.left:
                if prev and prev.val > cur.val:
                    if not first:
                        first = prev
                        middle = cur
                    else:
                        last = cur
                prev = cur
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                if pred.right is None:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    if prev and prev.val > cur.val:
                        if not first:
                            first = prev
                            middle = cur
                        else:
                            last = cur
                    prev = cur
                    cur = cur.right
        if last is None:
            first.val, middle.val = middle.val, first.val
        else:
            first.val, last.val = last.val, first.val
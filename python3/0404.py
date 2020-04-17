# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 求左叶子之和
        # 则关键在于如何判别该叶子节点是左侧节点
        # 因此，加入辅助bool值判断

        def searchLeaves(root: TreeNode, Left: bool):
            if not root:
                return 0
            if not root.left and not root.right:
                if Left:
                    return root.val
                else:
                    return 0
            else:
                return searchLeaves(root.left, True)+searchLeaves(root.right, False)

        if not root:
            return 0

        return searchLeaves(root.left, True)+searchLeaves(root.right, False)

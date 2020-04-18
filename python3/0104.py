# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        # 递归，其实是后序遍历，求出左节点的值与右节点的值比较取大值+1作为树根节点的值
        if not root:
            return 0
        ans = max(self.maxDepth1(root.left)+1, self.maxDepth1(root.right)+1)
        return ans

    def maxDepth2(self, root: TreeNode) -> int:
        # 前序遍历,先计算中间节点的值，再计算左右节点的值

        def travel(root, depth):
            if not root:
                return depth
            depth += 1
            l = travel(root.left, depth) if root.left else depth
            r = travel(root.right, depth) if root.right else depth

            return max(l, r)

        return travel(root, 0)

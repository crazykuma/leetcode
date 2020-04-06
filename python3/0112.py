# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 思路：考虑两种情况
        # 1. 节点还有子节点，则对子节点进行剩余的距离判断
        # 2. 节点不存在子节点，则对节点的值与剩余的距离进行判断
        # 其实还是一种后序遍历，先遍历左右节点的值，再遍历中间节点的值
        if not root:
            return False

        if not root.left and not root.right:
            # 到末端节点
            return sum-root.val==0
        # 未到末端节点
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

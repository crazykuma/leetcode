# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归分治
        # 如果树不存在，默认是对称的
        if not root:
            return True
        # 如果树存在，则判断其左右的子树是否对称
        return self.helper(root.left, root.right)

    def helper(self, left: TreeNode, right: TreeNode) -> bool:
        # 如果左树和右树都不存在，则返回真
        if not left and not right:
            return True
        # 如果左树和右树有一方不存在，则返回假
        if not left or not right:
            return False
        # 否则进行对称判断，判断条件是：
        # 1. 左树和右树的树根一致
        # 2. 左树的左子树和右树的右子树一致
        # 3. 左树的右子树和右树的左子树一致
        return (left.val == right.val) and self.helper(left.left, right.right) and self.helper(left.right, right.left)

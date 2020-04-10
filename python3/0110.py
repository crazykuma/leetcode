# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 验证平衡二叉树
        # 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
        # 一个平衡二叉树的两个子树也一定是平衡二叉树
        if not root:
            # 排出空树的情况
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            # 当左右子树都是平衡二叉树的时候，验证高度差不超过1
            return abs(self.Maxdepth(root.left)-self.Maxdepth(root.right))<=1
        else:
            # 当不满足左右子树都是平衡二叉树的时候，返回假
            return False


    def Maxdepth(self,root:TreeNode)-> int:
        # 求该节点的深度（高度）
        if not root:
            return 0
        
        return max(self.Maxdepth(root.left)+1,self.Maxdepth(root.right)+1)
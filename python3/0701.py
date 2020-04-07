# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 二叉搜索树的插入
        if not root:
            # 当树不存在时，返回以val为值的根节点
            return TreeNode(val)
        # 当树存在时
        if val < root.val:
            # 如果插入值比节点值小，向左查找
            if root.left:
                # 如果左边已经有节点，则继续向左查找
                self.insertIntoBST(root.left, val)
            else:
                # 如果左边没节点，则在左边插入节点
                root.left = TreeNode(val)
        if val > root.val:
            # 如果插入值比节点值大，向右查找
            if root.right:
                # 如果右边已经有节点，继续向右查找
                self.insertIntoBST(root.right, val)
            else:
                # 如果右边没有节点，则右边插入节点
                root.right = TreeNode(val)

        return root

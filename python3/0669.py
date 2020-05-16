# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        # dfs:前序遍历
        # 先对根节点进行剪枝
        if root.val < L:
            # 当根节点值小于最小边界L时
            # 根节点与左子树全都需要剪枝
            # 所以去右子树找新的根节点
            return self.trimBST(root.right, L, R)
        if root.val > R:
            # 当根节点值大于最大边界R时
            # 根节点与右子树全都需要剪枝
            # 去左子树寻找新的根节点
            return self.trimBST(root.left, L, R)
        # 当根节点值在[L,R]中时，对左右两子树进行剪枝
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        # 返回满足条件的根节点
        return root

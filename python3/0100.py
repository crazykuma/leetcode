# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归分治
        # 当两树都不存在，返回真
        if not p and not q:
            return True
        # 当一侧已经到空节点（末尾后一点）而另一侧非空时，返回假
        if not p or not q:
            return False
        # 当两树存在时，首先比较树根是否一致
        if p.val!=q.val:
            # 当树（子树）的根节点不一致，则返回false
            return False
        elif p.val==q.val:
            # 当树的根节点一致时，继续判断两侧的子树
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
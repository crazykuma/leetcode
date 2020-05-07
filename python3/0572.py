# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 判断子树，首先要找到子树的头节点位置
        # 如果s树的头结点就是t树的头节点，则逐项递归判断其左右节点是否相等
        # 如果s树的头节点不是t树的头节点，则在s树的子节点中继续寻找是否存在t树的头节点
        if not s:
            return False
        if self.compare(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def compare(self, s, t):
        # 比较两个节点是否相同
        # 标准：节点值，左右节点值
        if not s and not t:
            # 两个节点都不存在，为真（叶子节点下面的None节点）
            return True
        elif not s or not t:
            # 两个节点只有一个存在，为假
            return False
        else:
            # 两个节点都存在，则比较节点值，与左右节点
            # 叶子节点处：节点值，左右None，进入第一个if
            # 叶子节点处：节点值，左右只有一个none一致，则进入第二个if
            l_status = self.compare(s.left, t.left)
            r_status = self.compare(s.right, t.right)
            return s.val == t.val and l_status and r_status

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if t.left and t.right:
            return "{}({})({})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))
        elif t.left:
            return "{}({})".format(t.val, self.tree2str(t.left))
        elif t.right:
            return "{}()({})".format(t.val, self.tree2str(t.right))
        else:
            return "{}".format(t.val)

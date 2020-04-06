# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def travel(root):
            # 后序遍历，先访问左子树，再访问右子树，最后访问中间节点
            if not root:
                return res
            # left
            travel(root.left)
            # right
            travel(root.right)
            # middle
            res.append(root.val)

        travel(root)
        return res

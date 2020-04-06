# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def travel(root) -> List[int]:
            # 中序遍历，先左节点，根节点，然后右节点
            if not root:
                return res
            # left
            travel(root.left)
            # middle
            res.append(root.val)
            # right
            travel(root.right)

        travel(root)
        return res

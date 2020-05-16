# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []

        def dfs(root: TreeNode, res: List) -> None:
            if not root:
                return None

            dfs(root.left, res)          # left
            res.append(root.val)        # middle
            dfs(root.right, res)         # right
            return

        dfs(root, res)
        res = res[::-1]
        head = TreeNode(res.pop())
        p = head
        while res:
            p.right = TreeNode(res.pop())
            p = p.right

        return head

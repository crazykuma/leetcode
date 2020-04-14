from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        next_level = []
        r = []
        while queue:
            root = queue.pop(0)
            r.append(root.val)
            if root.left:
                next_level.append(root.left)
            if root.right:
                next_level.append(root.right)
            if not queue:
                queue = next_level
                next_level = []
                res.insert(0, r)
                r = []
        return res

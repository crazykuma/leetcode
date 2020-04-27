"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # N叉树的前序遍历
        if not root:
            return None
        res = []

        res.append(root.val)            # 中左右
        for node in root.children:
            res += self.preorder(node)

        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        res = []

        for node in root.children:
            res += self.postorder(node)

        res.append(root.val)
        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 求N叉树的最大深度
        def travel(root):
            if not root:
                return 0
            elif not root.children:
                return 1
            else:
                m = [travel(node) for node in root.children]
                return max(m)+1
        return travel(root)

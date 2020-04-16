from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def travel_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    # 如果已经到达叶子节点，则添加路径到列表中
                    paths.append(path)
                else:
                    # 如果没有到达叶子节点，则添加路径符号，并向子节点进行遍历
                    path += '->'
                    travel_paths(root.left, path)
                    travel_paths(root.right, path)

        paths = []
        travel_paths(root, '')
        return paths

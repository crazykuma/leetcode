# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 前序遍历，首先访问根节点，然后访问左节点，然后访问右节点
        # 框架如下
        # if not root:
        #     return 
        # print(root.val)
        # self.preorderTraversal(root.left)
        # self.preorderTraversal(root.right)
        # 现在要加入一个result=[]来记录遍历的值，那么修改上面的框架为
        result = []

        def travel(root: TreeNode) -> List[int]:
            if not root:
                return result
            result.append(root.val)
            travel(root.left)
            travel(root.right)
            
        travel(root)

        return result
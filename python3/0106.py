# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 由后序遍历和中序遍历构造二叉树
        # 由于后序遍历是左右根，所以后序遍历的最后一个值即为根节点a
        # 而中序遍历是左根右，所以根据后序遍历得到的根节点位置，可以分为左子树和右子树s0,a,s1
        # 根据左右子树的长度（深度）在后序遍历[t,a]中将s分为[t0,t1,a]再对t0和t1分别进行上述操作
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:idx], postorder[0:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return root


if __name__ == "__main__":
    s = Solution()
    s.buildTree([9, 3, 15, 20, 7],
                [9, 15, 7, 20, 3])

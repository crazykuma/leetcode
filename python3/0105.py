from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前序遍历与中序遍历构造二叉树
        # 前序遍历第0位一定是根节点a，因此可以分为[a,s]
        # 根据找到的根节点a在中序遍历m中寻找，可以分为[m1,a,m2]
        # 根据找到的m1和m2长度再划分s为s1和s2作为新的前序遍历
        # 将s1作为前序，m1作为中序建立子树，s2,m2同样
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:idx+1], inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root


if __name__ == "__main__":
    s = Solution()
    s.buildTree([3, 9, 20, 15, 7],
                [9, 3, 15, 20, 7])

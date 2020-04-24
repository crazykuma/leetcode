""" 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。 """

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # DFS
        def search(root, L, R):
            if not root:
                return 0

            l = search(root.left, L, R)
            r = search(root.right, L, R)
            # 关键语句就这一句，范围内的值被选取，范围外的值都返回0
            ans = root.val if L <= root.val <= R else 0
            return ans+l+r

        return search(root, L, R)

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:

        def search(root, L, R):
            if not root:
                return 0

            if root.val < L:
                # root.val <L ,因为root.left<root.val因此，left子树都不用查找了
                return search(root.right, L, R)
            elif root.val > R:
                # root.val >R,因为root.right>root.val>R,right子树也不用找了
                return search(root.left, L, R)
            else:
                # L<=root.val<=R
                return root.val+search(root.left, L, R)+search(root.right, L, R)

        return search(root,L,R)

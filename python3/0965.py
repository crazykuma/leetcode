# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # 单值二叉树
        # 判断左侧子节点和右侧子节点是否与父节点值相等
        # 左右都满足相等||或者左右子节点不存在时为真
        # 左右有一个不满足相等即为假
        # 36ms:79.20%
        # 13.7mb:100%

        def dfs(root):
            if not root:
                return

            left_res = (not root.left) or (
                root.left.val == root.val and dfs(root.left))
            right_res = (not root.right) or (
                root.right.val == root.val and dfs(root.right))
            return left_res and right_res

        def dfs2(root):
            # dfs等价于dfs2，但是dfs的写法更简洁且更容易理解
            if not root:
                return

            if not root.left and not root.right:
                return True
            if root.left and not root.right:
                return root.left.val == root.val and dfs(root.left)
            if root.right and not root.left:
                return root.right.val == root.val and dfs(root.right)
            if root.right and root.left:
                return root.left.val == root.right.val == root.val and (
                    dfs(root.left) and dfs(root.right))

        return dfs(root)

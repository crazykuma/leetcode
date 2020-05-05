# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 深度优先搜索DFS
        # 60ms
        # 15.8mb

        def dfs(root, min_val, max_val):
            """深度优先搜索

            Arguments:
                root {TreeNode} -- parent node
                min_val {float} -- lower_limit
                max_val {float} -- upper_limit

            Returns:
                bool -- valid status of BST
            """
            if not root:
                return True

            if root.val >= max_val or root.val <= min_val:
                # 当子节点的值超出父节点的上下边界时，不是BST
                return False
            else:
                return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

        return dfs(root, float("-inf"), float("inf"))

    def isValidBST2(self, root: TreeNode) -> bool:
        # 60ms:49.97%
        # 16.7mb:9.52%
        # 中序遍历法：因为中序遍历得到的序列必然是升序，不满足升序的序列就不是BST
        res = []

        def inorder(root):
            if not root:
                return None
            # 左
            inorder(root.left)
            # 中
            res.append(root.val)
            # 右
            inorder(root.right)
            return

        inorder(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False

        return True

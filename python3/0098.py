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

    def isValidBST3(self, root: TreeNode) -> bool:
        # 根据方法2中序遍历完成后再判断，可以进一步优化为
        # 中序遍历+在递归过程中判断前后值，用数组也可以，这里不用数组
        # 64ms:37.70%
        # 16.4mb:9.52%
        pre = float("-inf")

        def inOrder(root):
            nonlocal pre
            if not root:
                return True

            if not inOrder(root.left):
                # 当左子节点不满足中序遍历时返回False
                return False
            if root.val <= pre:
                # 当前节点不满足中序遍历时返回False
                return False
            else:
                # 当前节点满足中序遍历，将当前节点的值赋给pre作为前值
                pre = root.val
            if not inOrder(root.right):
                # 当右子节点不满足中序遍历时返回False
                return False
            # 当所有遍历都完成且满足中序遍历，返回True
            return True

        return inOrder(root)

    def isValidBST4(self, root: TreeNode) -> bool:
        # 中序遍历+数组+中间判断的解法
        # 56ms:65.11%
        # 16.4mb：9.52%
        res = [float("-inf")]

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= res[-1]:
                return False
            else:
                res.append(root.val)
            if not inorder(root.right):
                return False
            return True

        return inorder(root)

    def isValidBST5(self, root: TreeNode) -> bool:
        # 中序遍历+栈+迭代
        # 56ms:65.11%
        # 16mb:9.52%
        if not root:
            return True
        stack = []
        prev = float("-inf")
        p = root              # 指针

        while p or stack:
            # push
            while p:
                # 将当前节点及其左子节点都加入栈中
                stack.append(p)
                p = p.left

            # pop
            p = stack.pop()
            if p.val <= prev:
                # 比较当前节点与前值
                return False

            prev = p.val

            # 指针指向右子节点
            p = p.right
        return True

    def isValidBST6(self, root: TreeNode) -> bool:
        # 中序遍历+yield法+迭代法
        # 64ms:37.70%
        # 16.5mb：9.52%

        def yieldTree(root: TreeNode) -> TreeNode:
            # yield法中序遍历
            # yield生成一个可迭代对象，每次代码运行到yield后暂停，下次迭代时继续
            if root.left:
                for i in yieldTree(root.left):
                    yield i
            yield root.val

            if root.right:
                for i in yieldTree(root.right):
                    yield i

        if not root:
            return True

        pre = float("-inf")
        for cur in yieldTree(root):
            if cur <= pre:
                return False
            else:
                pre = cur

        return True

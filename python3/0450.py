# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 删除节点有3种情况
        # 该节点无子节点：直接删除
        # 该节点有1个子节点，删除该节点并让子节点补上:左侧应选比root小的最大值；右侧应选比root大的最小值
        # 该节点有两个子节点，删除该节点后，从左侧或右侧选择一个补上都可
        def findminright(root):
            # 在右侧找到比root大的最小值
            root = root.right
            while root.left:
                root = root.left
            return root.val

        def findmaxleft(root):
            # 在左侧找到比root小的最大值
            root = root.left
            while root.right:
                root = root.right
            return root.val

        if not root:
            return None

        if key < root.val:
            # 左侧删除
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # 右侧删除
            root.right = self.deleteNode(root.right, key)
        else:
            # 是要删除的节点
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = findmaxleft(root)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = findminright(root)
                root.right = self.deleteNode(root.right, root.val)

        return root

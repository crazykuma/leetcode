# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, vals: List[int]):
        if not vals:
            self.root = []
        self.root = TreeNode(vals.pop(0))
        cur = [self.root]
        while vals and cur:
            node = cur.pop(0)
            if vals[0] is not None:
                node.left = TreeNode(vals.pop(0))
                cur.append(node.left)
            else:
                vals.pop(0)

            if vals[0] is not None:
                node.right = TreeNode(vals.pop(0))
                cur.append(node.right)
            else:
                vals.pop(0)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 36ms
        # 二叉树的层序遍历
        # 首先访问节点本身
        # 然后遍历他的相邻节点
        if not root:
            # 如果树不存在，则返回空列表
            return []

        res = []
        level = [root]            # 记录第一层

        def travel(level):
            nextlevel = []       # 记录下一层
            value = []           # 记录该层的值列表
            for t in level:    # 对当前层的每一个节点进行遍历
                if t.left:     # 生成下一层的内容
                    nextlevel.append(t.left)
                if t.right:
                    nextlevel.append(t.right)
                value.append(t.val)      # 记录当前层每一项的值
            if value:
                res.append(value)        # 当前层不为空时，记录当前层的值
            if nextlevel:
                travel(nextlevel)        # 下一层为空时停止遍历

        travel(level)  # 从第一层开始遍历
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        # 32ms:96.81%
        # 队列
        if not root:
            return []
        res = []
        values = []
        stack = [root]
        nextlevel = []
        while stack:
            node = stack.pop(0)
            values.append(node.val)
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
            if not stack:
                stack = nextlevel
                res.append(values)
                values = []
                nextlevel = []

        return res


if __name__ == "__main__":
    s = Solution()
    tree1 = Tree([3, 9, 20, None, None, 15, 7])
    tree2 = Tree([1, 2, 3, 4, 5])
    print(s.levelOrder2(tree1.root))
    print(s.levelOrder2(tree2.root))

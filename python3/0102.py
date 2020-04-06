# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

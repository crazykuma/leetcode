# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 超时
        # 思路：
        # 给定一个二叉树的根节点，再给定两个子节点
        # 通过分别查找两个子节点的途径路径，得到两个序列a,b
        # 对a,b从右侧开始查找共同点，找到的即为最近公共祖先
        if not root:
            return None
        pPath = self.route(root, p, [])
        qPath = self.route(root, q, [])
        common = [v for v in pPath if v in qPath]
        return common[-1]

    def route(self, root: 'TreeNode', p: 'TreeNode', res: List) -> List[int]:
        # 查找子节点的途径路径
        # 如果根节点为空，返回
        if not root:
            return res
        # 先判断值是否相等，如果相等则认为已经找到目标，返回包含当前节点值的结果
        if root.val == p.val:
            res.append(root)
            return res
        # 如果值不相等，则判断是否有下一层，如果没有下一层，则返回不包含当前节点值的结果
        else:
            if not root.left and not root.right:
                return res
            # 如果还有下一层，那么同时进行左右两边的寻路,默认先找左边，如果左边找到了，右边就不再寻找
            # 如果左边没找到，则在当前节点的基础上继续查找右边
            else:
                res.append(root)
                a = res[:]
                b = res[:]

                lPath = self.route(root.left, p, a)
                if p in lPath:
                    return lPath
                else:
                    rPath = self.route(root.right, p, b)
                    return rPath

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 超时
        # 思路：
        # 给定一个二叉树的根节点，再给定两个子节点
        # 给定一个路径从根节点开始分别查找两个的路径
        # 用层序遍历定位各处在第几层，然后由叶子节点开始构建二叉树路径，比较公共位置
        if not root:
            return None
        pPath = self.route2(root, p)
        qPath = self.route2(root, q)
        common = [v for v in pPath if v in qPath]
        return common[0]

    def route2(self, root, p):
        node = [root]
        levels = [node]
        res = []
        while node:
            n = len(node)
            queue = []
            if p in node:
                break
            for i in range(n):
                if node[i].left:
                    queue.append(node[i].left)
                else:
                    queue.append(TreeNode(None))
                if node[i].right:
                    queue.append(node[i].right)
                else:
                    queue.append(TreeNode(None))
            node = queue
            levels.append(queue)

        n = len(levels)
        idx = levels[-1].index(p)
        for i in range(n-1, -1, -1):
            res.append(levels[i][idx])
            idx = idx//2

        return res

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 阅读题解后：
        # 递归法

        def route3(root, p, q):
            if not root:
                # 排除树为空的情况
                return None
            if root == p or root == q:
                # root是所有的共同祖先，如果有一方是root，那最短公共祖先一定是root
                return root
            # 如果root不是最短公共祖先，那就在左树和右树寻找
            left = route3(root.left, p, q)
            right = route3(root.right, p, q)
            # 如果只有一方返回的值为真，则返回值就是最短公共祖先
            # 如果两方返回的值都是真，则最短公共祖先为root（pq分散在左右子树中）
            if left and right:
                return root
            else:
                return left if left else right

        return route3(root, p, q)

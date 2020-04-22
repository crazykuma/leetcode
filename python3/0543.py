# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

    示例 :
    给定二叉树

             1
            / \
           2   3
          / \    
         4   5    
    返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 对任意一个节点，一定有最长路径穿过当前节点
        # 最长路径=左节点最大深度+右节点最大深度
        maxDepth = 0

        def depth(root):
            nonlocal maxDepth
            if not root:
                return -1
            L = depth(root.left)+1             # 取左节点的最大深度
            R = depth(root.right)+1            # 取右节点的最大深度
            maxDepth = max(L+R, maxDepth)      # 更新最长路径
            return max(L, R)                   # 返回当前节点单边的最大深度

        depth(root)
        return maxDepth

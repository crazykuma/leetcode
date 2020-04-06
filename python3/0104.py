# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        # 递归，其实是后序遍历，求出左节点的值与右节点的值比较取大值+1作为树根节点的值
        if not root:
            return 0
        ans = max(self.maxDepth1(root.left)+1,self.maxDepth1(root.right)+1)
        return ans
            
    def maxDepth2(self, root: TreeNode) -> int:
        # 前序遍历，记录下每个节点的深度，然后取最大
        res=[0]
        
        def travel(root,depth):
            if not root:
                return max(res)
            depth+=1
            res.append(depth)
            if root.left:
                travel(root.left,depth)
            if root.right:
                travel(root.right,depth)
            
        travel(root,0)
        return max(res)
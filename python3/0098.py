# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 判断条件
        # 在左子树中找最大值，与root比，要小于
        # 在右子树中找最小值，与root比，要大于
        
        def search(root,min_val,max_val):
            if not root:
                return True
            
            if root.val>=max_val or root.val <= min_val:
                return False
            else:
                return search(root.left,min_val,root.val) and search(root.right,root.val,max_val)
        
        return search(root,float("-inf"),float("inf"))
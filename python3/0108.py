from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 有序数组转换成平衡二叉搜索树
        # 因为有序数组就是二叉搜索树的中序排列，因此，可以将有序数组分成[left,root.val,right]三部分
        # 又因为平衡二叉树左右深度差不超过1，所以left和right的长度应该尽可能的相等，因此有序数组的中间位置即是root的值
        if not nums:
            return None
        mid_idx = len(nums)//2
        mid = nums[mid_idx]
        left_array = nums[0:mid_idx]
        right_array = nums[mid_idx+1:]
        root = TreeNode(mid)
        if len(left_array) > 0:
            root.left = self.sortedArrayToBST(left_array)
        else:
            root.left = None
        if len(right_array) > 0:
            root.right = self.sortedArrayToBST(right_array)
        else:
            root.right = None

        return root

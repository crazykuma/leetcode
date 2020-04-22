from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找法
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1


        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # 左边是升序序列
                if nums[left] <= target <= nums[mid]:
                    # 在左边，收缩右边界，查找范围[left,mid), nums[mid]!=target
                    right = mid-1
                else:
                    # 在右边，查找范围(mid,right]
                    left = mid+1
            elif nums[mid] <= nums[right]:
                # 右边是升序序列
                if nums[mid] <= target <= nums[right]:
                    # 在右边，收缩左边界，查找范围(mid,right]
                    left = mid+1
                else:
                    # 在左边，收缩右边界，查找范围[left,right)
                    right = mid-1

        # 都查不到，返回-1
        return -1

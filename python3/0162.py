from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """峰值元素是指其值大于左右相邻值的元素。
        给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
        数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        n = len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            n_left = nums[mid-1] if mid >= 1 else float("-inf")
            n_right = nums[mid+1] if mid < n-1 else float("-inf")
            if nums[mid] > n_left and nums[mid] > n_right:
                return mid
            elif nums[mid] < n_right:
                # 峰值在右，更新左边界
                left = mid+1
            elif nums[mid] < n_left:
                # 峰值在左，更新右边界
                right = mid-1

        return left


if __name__ == "__main__":
    s = Solution()
    assert s.findPeakElement([1, 2, 3]) == 2
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]

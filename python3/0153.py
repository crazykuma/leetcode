from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                # 用右边界做判断很讨巧         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]

    def findMin2(self, nums:List[int])-> int:
        n = len(nums)
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right)//2
            n_left = nums[mid-1] if mid >= 1 else float("inf")
            n_right = nums[mid+1] if mid < n-1 else float("inf")
            if nums[mid] < n_left and nums[mid] < n_right:
                return nums[mid]
            if nums[left] < nums[right]:
                # [0,1,2,3,4]片段中升序排列
                return nums[left]

            elif nums[left] <= nums[mid]:
                # 左边[left,mid]是连续的[3,4,5,6,0,1,2]
                # 查找右边(mid,right]
                left = mid+1
            elif nums[mid] <= nums[right]:
                # 右边是连续的
                # 查找左边
                right = mid




if __name__ == "__main__":
    s = Solution()
    print(s.findMin2([0]))
    print(s.findMin2([5, 1, 2, 3, 4]))  # 1
    print(s.findMin2([3, 4, 5, 1, 2]))  # 1
    print(s.findMin2([0, 1, 2, 3, 4]))  # 0
    print(s.findMin2([1, 2, 3, 4, 0]))  # 0

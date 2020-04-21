from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        mid = (i+j)//2
        while j >= i:
            if target > nums[mid]:
                i = mid+1
                mid = (i+j)//2
            elif target < nums[mid]:
                j = mid-1
                mid = (i+j)//2
            else:
                return mid
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([5], 5))
    print(s.search([5], -5))
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        sums=sum(nums)
        for i in range(len(nums)):
            index=nums[i]
            right = sums-index-left
            if left==right:
                return i
            left+=index
        else:
            return -1

if __name__ == "__main__":
    s=Solution()
    print(s.pivotIndex([1,2,3]))
    print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
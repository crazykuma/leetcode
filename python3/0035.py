from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 48ms beat 99.98% python3
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
            else:
                return len(nums)


if __name__ == "__main__":
    s=Solution()
    print(s.searchInsert([1,3,5,6],5))
    print(s.searchInsert([1,3,5,6],2))
    print(s.searchInsert([1,3,5,6],7))
    print(s.searchInsert([1,3,5,6],0))
    print(s.searchInsert([],0))
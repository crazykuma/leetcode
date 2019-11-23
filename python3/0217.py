from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        if len(s)==len(nums):
            return False
        else:
            return True

if __name__ == "__main__":
    s=Solution()
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,2,3,1]))
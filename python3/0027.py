from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)

if __name__ == "__main__":
    s=Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2],2))
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while(i<n-1):
            if(nums[i]==nums[i+1]):
                nums.pop(i+1)
            else:
                i+=1
            n=len(nums)
        return n

if __name__ == "__main__":
    newlist=eval(input("please input list:"))
    s=Solution()
    print(s.removeDuplicates(newlist))
    print(newlist)
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        maxCount=0
        count=0
        while i<len(nums):
            if i!=len(nums)-1:
                if nums[i]==1:
                    count+=1
                else:
                    if count>maxCount:
                        maxCount=count
                    count=0
            else:
                if nums[i]==1:
                    count+=1
                if count>maxCount:
                    maxCount=count
            i+=1
        return maxCount

    def findMaxConsecutiveOnes2(self,nums:List[int])->int:
        count=0
        maxCount=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxCount=max(maxCount,count)
            else:
                count=0
        return maxCount


if __name__ == "__main__":
    s=Solution()
    print(s.findMaxConsecutiveOnes2([1]))
    print(s.findMaxConsecutiveOnes2([1,1,0,1,1,1,0]))

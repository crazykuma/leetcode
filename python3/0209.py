from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 84ms > 99.38%
        x=sum(nums)
        if s>x:
            return 0
        elif s==x:
            return len(nums)
        else:
            # 滑动窗口法，从左向右
            # 定义左指针和右指针位置之间的部分为计数的窗口
            # 当计数和大于s时，对左侧窗口进行移动，记录满足条件的最小窗口长度
            # 当右指针指到末尾，且左指针移动到不能移动时，便是遍历了所有满足条件的窗口，返回最小窗口长度
            left=0
            total=0
            minCount=len(nums)
            for right in range(len(nums)):
                total+=nums[right]
                while total >=s:
                    minCount=min(minCount,right-left+1)
                    total-=nums[left]
                    left+=1
            return minCount



if __name__ == "__main__":
    s=Solution()
    print(s.minSubArrayLen(s=11,nums=[1,2,3,4,5])) #5,4,3=3
    print(s.minSubArrayLen(s=7,nums=[2,3,1,2,4,3])) #4,3=2
    print(s.minSubArrayLen(s=14,nums=[1,2,3,4,5,4,2,3])) #3,4,5,4// 4,5,4,2

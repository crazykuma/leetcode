from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # 用列表
        i=0
        n=len(nums)
        while(i<n-1):
            diff=target-nums[i]
            if diff in nums[i+1:]:
                break
            else:
                i+=1
        return [i,nums[i+1:].index(diff)+i+1]

    def twoSum2(self, nums:List[int], target: int) -> List[int]:
        # 用字典
        d={}
        for i,n in enumerate(nums):
            if target-n in d:
                return [d.get(target-n),i]
            d[n]=i


if __name__ == "__main__":
    s=Solution()
    print(s.twoSum1([3,3],6))
    print(s.twoSum2([3,3],6))
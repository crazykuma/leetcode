from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i,n in enumerate(nums):
            if d.get(n,0):
                # 存在
                d.pop(n)
            else:
                # 不存在
                d[n]=i
        
        return d.popitem()[0]


if __name__ == "__main__":
    s=Solution()
    print(s.singleNumber([4,1,2,1,2]))
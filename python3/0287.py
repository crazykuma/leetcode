from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
            if d[n]>1:
                return n

if __name__ == "__main__":
    s=Solution()
    print(s.findDuplicate([1,3,4,2,2]))
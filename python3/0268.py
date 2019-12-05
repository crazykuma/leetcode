from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 160ms beat 96.51% python3
        n=len(nums)+1
        s=set([i for i in range(n)])
        b=set(nums)
        return (s-b).pop()

if __name__ == "__main__":
    s=Solution()
    print(s.missingNumber([3,0,1]))
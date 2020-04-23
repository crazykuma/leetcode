from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(n)%2==0 for n in [str(c) for c in nums]])


if __name__ == "__main__":
    s=Solution()
    assert s.findNumbers([12,345,2,6,7896])==2



from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i*i for i in A])


if __name__ == "__main__":
    s=Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
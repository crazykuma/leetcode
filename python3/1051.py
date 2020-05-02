from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = sum([heights[i] != sorted(heights)[i]
                 for i in range(len(heights))])
        return n

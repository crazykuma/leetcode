from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针解法
        maxpool = float("-inf")
        i = 0
        j = len(height)-1
        while i < j:
            # 矩形公式，长=（j-i），宽=最短边的长
            poolsize = (j-i)*min(height[i], height[j])
            maxpool = max(maxpool, poolsize)
            if height[i] < height[j]:
                # 因为每次长都会缩减1，那么要让水变多
                # 关键在于让最短边更长，增加的面积=(j-i-1)*(height1-height2)
                i += 1
            else:
                j -= 1
        return maxpool


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

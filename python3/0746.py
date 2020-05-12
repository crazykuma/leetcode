from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 动态规划
        n = len(cost)
        dp = [0 for _ in range(len(cost)+1)]
        # 从2开始是因为第1格无需体力，只有爬上第2格才需要第1格的耗费体力
        for i in range(2, len(dp)):
            # 因为每一步都可以选择爬1-2个阶梯，所以取上一个阶梯和上两个阶梯分别加上其耗费体力取更小值
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

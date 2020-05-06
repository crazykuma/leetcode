from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 动态规划
        # 52ms:68%
        # 13.6mb:33.3%
        # 记录第0天到第n天的最少价格
        dp = [0 for _ in range(days[-1]+1)]
        point = 0  # 所在位置
        for i in range(1, len(dp)):
            if i != days[point]:
                # 当第i天不是要旅行的日子，那么继承上一日的费用
                dp[i] = dp[i-1]
            else:
                # 当第i天是要旅行的日子，那么比较从i-T天的价格加上T天的票价，T是时间窗口
                # 因为求的是最低消费，所以选取最小值,max是防止数组越界,数组下标最小值应该为0
                price0 = dp[max(0, i-1)]+costs[0]  # cost0
                price1 = dp[max(0, i-7)]+costs[1]  # cost1
                price2 = dp[max(0, i-30)]+costs[2]  # cost2
                dp[i] = min(price1, price2, price0)
                # 要求的日期指针向后移动1格
                point += 1

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))

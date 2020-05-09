from typing import List


class NumArray:
    # 笨办法，暴力解，每次sumRange的时候重新计算
    # 6588ms：9.32%
    # 17.2mb：20.69%
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)

    def sumRange(self, i: int, j: int) -> int:
        s = 0
        for k in range(i, j+1):
            s += self.nums[k]

        return s


class NumArray2:
    # 动规思路
    # 用数组计算逐项求和
    # 计算两项之间的和变成计算两项之间的差
    # dp[i]=dp[0]+dp[1]+...+dp[i-1]
    # dp[j+1]=dp[0]+dp[1]+...dp[i-1]+dp[i]+...+dp[j-1]+dp[j]
    # 计算第j项到第i项则是dp[i]+dp[i+1]+...+dp[j-1]+dp[j]
    # 因此dp[j+1]-dp[i]就是要求的两项之间的和
    # 132ms:51.87%
    # 17.5mb:17.24%
    def __init__(self, nums: List[int]):
        self.dp = [0]*(len(nums)+1)
        self.dp[0] = 0
        for i in range(1, len(self.dp)):
            self.dp[i] = self.dp[i-1]+nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]


if __name__ == "__main__":
    s = NumArray2([-2, 0, 3, -5, 2, -1])
    assert s.sumRange(0, 2) == 1
    assert s.sumRange(2, 5) == -1
    assert s.sumRange(0, 5) == -3

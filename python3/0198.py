from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 当前位置的最大值=max(上一个位置的值，上两个位置的值+当前这个位置的值)
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[len(nums)]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2, 1, 1, 2]))

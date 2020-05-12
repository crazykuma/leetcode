class Solution:
    def climbStairs(self, n: int) -> int:
        # 超出时间限制
        # 其实跟斐波那契数列一模一样
        # 1 1 2 3 5 8 13 .....
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs2(self, n: int) -> int:
        # 36ms
        a = 1
        b = 2
        if n == 1:
            return a
        elif n == 2:
            return b
        else:
            for _ in range(2, n):
                # 1 2 3 5 8
                a, b = b, a+b
            return b

    def climbStairs3(self, n: int) -> int:
        # 动态规划
        # 第n个台阶只能从第n-1和第n-2个台阶上来
        # 因此状态方程dp[n]=dp[n-1]+dp[n-2]
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(38))

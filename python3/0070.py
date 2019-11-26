class Solution:
    def climbStairs(self, n: int) -> int:
        # 超出时间限制
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs2(self, n: int) -> int:
        # 36ms
        a=1
        b=2
        if n==1:
            return a
        elif n==2:
            return b
        else:
            for _ in range(2,n):
                # 1 2 3 5 8
                a,b=b,a+b
            return b

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(38))

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def fastpow(x: float, n: int) -> float:
            """快速幂
            n是偶数：(x^2n)=(x^n)^2
            n是奇数,n=2k+1：(x^(2k+1))=(x^n)^2*x
            Arguments:
                x {float} -- 底数
                n {int} -- 幂

            Returns:
                float -- result
            """
            if n == 0:
                return 1.0
            halfpow = fastpow(x, n//2)
            if n % 2 == 0:
                return halfpow*halfpow
            else:
                return halfpow*halfpow*x

        return fastpow(x, n) if n >= 0 else fastpow((1/x), abs(n))


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2, 10))
    print(s.myPow(2, -2))
    print(s.myPow(1.00001, 123456))

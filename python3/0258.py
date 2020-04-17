class Solution:
    def addDigits(self, num: int) -> int:
        # 递归
        if num < 10:
            return num
        num = sum([int(i) for i in str(num)])
        return self.addDigits(num)

    def addDigits2(self, num: int) -> int:
        # 循环
        s = 0
        while num > 10:
            a, b = divmod(num, 10)
            s += b
            if a < 10:
                s += a
                num = s
                s = 0
        else:
            return num

    def addDigits3(self, num: int) -> int:
        # 数学归纳
        # 1. 任何只包含1和0的数字的最终结果都是1，因此可以分解成1+9*N，M-1=9*N+0
        # 2. 任何只包含2个1和其他都是0的数字的最终结果都是2，因此可以分解成1+1+9*N，M-1=9*N+1
        # 3. 依次类推，当包含9个1时，存在1*9+9*N=M，考虑该特殊情况，M-1=9*N+8
        # 归纳 K个1的情况，K-1=(M-1)%9,K=(M-1)%9+1
        # 扩展到任何数，其实每一位都是0或者1的和，因此11和20是一样的，111和300是一样的，以此类推
        return (num-1)%9+1

if __name__ == "__main__":
    s = Solution()
    print(s.addDigits2(18))

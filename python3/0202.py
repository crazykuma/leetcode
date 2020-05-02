class Solution:
    def isHappy(self, n: int) -> bool:
        # 暴力求解，给定循环次数
        i = 0
        while i < 100:
            n = self.calsquaresum(n)
            i += 1
            if n == 1:
                return True
        else:
            return False

    def calsquaresum(self, n: int) -> int:
        # 比n = sum([int(i)**2 for i in str(n)])要快
        s = 0
        while n > 0:
            m = n % 10
            n = n//10
            s = s+pow(m, 2)

        return s

    def isHappy2(self, n: int) -> bool:
        # 使用集合set()方法
        d = set()
        while n != 1:
            # n = sum([int(i)**2 for i in str(n)])
            n = self.calsquaresum(n)
            if n not in d:
                d.add(n)
            else:
                return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy2(8))

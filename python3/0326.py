class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 递归法
        # 88ms:75.77%
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n//3)
        else:
            return False

    def isPowerOfThree2(self, n: int) -> bool:
        # 循环法
        # 68ms:98.01%
        if n == 0:
            return False
        while n % 3 == 0:
            n = n//3
        return n == 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree2(0))

class Solution:
    '给定一个整数，编写一个函数来判断它是否是 2 的幂次方。'

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False

        while n % 2 == 0:
            n = n//2
        else:
            if n == 1:
                return True
            else:
                return False

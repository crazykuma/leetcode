class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # 循环法
        if num == 0:
            return False
        while num % 4 == 0:
            num = num//4
        return num == 1

    def isPowerOfFour2(self, num: int) -> bool:
        # 递归法
        if num == 0:
            return False
        if num == 1:
            return True
        if num % 4 == 0:
            return self.isPowerOfFour(num//4)
        else:
            return False

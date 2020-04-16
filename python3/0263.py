class Solution:
    def isUgly(self, num: int) -> bool:
        # 递归法
        s = [2, 3, 5]
        if num == 0:
            return False
        if num == 1 or num in s:
            return True
        if num % 2 == 0:
            return self.isUgly(num//2)
        if num % 3 == 0:
            return self.isUgly(num//3)
        if num % 5 == 0:
            return self.isUgly(num//5)
        return False

    def isUgly2(self, num: int) -> bool:
        # 迭代
        if num == 0:
            return False
        while num != 1:
            if num % 2 == 0:
                num = num//2
            elif num % 3 == 0:
                num = num//3
            elif num % 5 == 0:
                num = num//5
            else:
                return False

        return True

if __name__ == "__main__":
    s=Solution()
    print(s.isUgly2(18))
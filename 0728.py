from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def selfDivid(num):
            n = num
            while num > 0:
                m = num % 10
                if m == 0 or n % m != 0:
                    return False
                num //= 10
            return True
        res = []

        for i in range(left, right+1):
            if selfDivid(i):
                res.append(i)

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.selfDividingNumbers(1, 11) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # 与汉明距离是同一个问题
        # 布莱恩·克尼根算法
        # 通过n&(n-1)消去最后1位的1
        res = []
        for i in range(num+1):
            distance = 0
            xor = i ^ 0
            while xor:
                distance += 1
                xor = xor & (xor-1)
            res.append(distance)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))

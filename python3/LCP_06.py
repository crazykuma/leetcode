from typing import List
"""桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

"""

class Solution:
    def minCount(self, coins: List[int]) -> int:
        count = 0
        for n in coins:
            while n > 0:
                count += 1
                n = n-2

        return count

if __name__ == "__main__":
    s=Solution()
    print(s.minCount([4,2,1]))
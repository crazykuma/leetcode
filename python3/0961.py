from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # 2N的数组中右N个一样的元素，剩下N个元素都不一样
        # 因此，其他所有的元素数量都是1个
        # 采用哈希表或集合,当出现过在集合中的元素时，就是要找的数
        d = set()
        for n in A:
            if n not in d:
                d.add(n)
            else:
                return n


if __name__ == "__main__":
    s = Solution()
    assert s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5

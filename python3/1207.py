""" 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。 """


from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 用哈希表比较键值的数量是否相等
        d = {}
        for num in arr:
            d[num] = d.get(num, 0)+1

        rd = {v: k for k, v in d.items()}
        return len(d) == len(rd)


if __name__ == "__main__":
    s = Solution()
    assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True

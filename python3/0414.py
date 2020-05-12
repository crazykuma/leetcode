from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 用集合跳过重复的数字，将剩下的进行排序
        # 也可以维护一个长度为3的数组或列表
        # 要求算法复杂度为O(N)
        first = second = third = float("-inf")
        visit = set()
        for n in nums:
            if n not in visit:
                visit.add(n)
            else:
                continue
            if n > third:
                if n > second:
                    if n > first:
                        first, second, third = n, first, second
                    else:
                        second, third = n, second
                else:
                    third = n
        if third != float("-inf"):
            return third
        else:
            return first


if __name__ == "__main__":
    s = Solution()
    assert s.thirdMax([3, 2, 1]) == 1
    assert s.thirdMax([1, 1, 2]) == 2
    assert s.thirdMax([2, 2, 3, 1]) == 1

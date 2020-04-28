from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # 桶排序
        array = [0]*101
        total = 0
        for n in nums:
            array[n] += 1
            total += n

        res = []
        cur = 0
        for i in range(100, 0, -1):
            while array[i] > 0:
                res.append(i)
                array[i] -= 1
                cur += i
                total -= i
                if cur > total:
                    return res


if __name__ == "__main__":
    s = Solution()
    assert s.minSubsequence([4, 3, 10, 9, 8]) == [10, 9]
    assert s.minSubsequence([4, 4, 7, 6, 7]) == [7, 7, 6]

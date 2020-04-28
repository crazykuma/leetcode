""" 示例 1：

输入：nums = [-3,2,-3,4,2]
输出：5
解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                累加求和
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

 """


from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        sum_tmp = startValue
        for n in nums:
            sum_tmp += n
            while sum_tmp < 1:
                startValue += 1
                sum_tmp += 1

        return startValue


if __name__ == "__main__":
    s = Solution()
    assert s.minStartValue([-3, 2, -3, 4, 2]) == 5

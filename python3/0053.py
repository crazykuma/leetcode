from typing import List
'''
思路：
首先考虑笨办法，即排出所有的NXN矩阵，则每一子段的距离都可以在矩阵的交点处得到，
问题就变成了求所有矩阵交点中最大的点，但是这种方法时间复杂度是O(N^2)。
然后化简该方法，即只需要从起点开始计算到下一点的值之和与该点的值比较，
每一段取其大值继续往下计算（类似寻路算法），记录下每次得到的值与前值进行比较，得到最大值。
该最大值即所要求的最大子序和。（局部最长路径），该方法时间复杂度为O(N)
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 60ms
        s = nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            # s=s+nums[i] if s+nums[i] > nums[i] else nums[i]
            s = max(s+nums[i], nums[i])
            m = max(m, s)

        # 不使用max反而会更快一点,是因为考虑到if条件语句的选择忽略特点
        # 44ms,90.55%
        # for n in nums[1:]:
        #     s = s+n if s > 0 else n
        #     m = s if s > m else m

        return m


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-1, -2]))
    print(s.maxSubArray([-2, -1, 3, 4]))
    print(s.maxSubArray([-2, 1]))

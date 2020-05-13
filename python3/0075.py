""" 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """

from typing import List

case1 = [2, 0, 2, 1, 1, 0]
case2 = [0]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 桶排序
        bucket = [0, 0, 0]   # 3个颜色桶，分别对0，1，2计数
        for color in nums:
            bucket[color] += 1
        j = 0
        for i in range(3):
            while bucket[i] > 0:
                nums[j] = i
                bucket[i] -= 1
                j += 1
        return

    def sortColors2(self, nums: List[int]) -> None:
        # 一次遍历
        # 因为仅有3个数字，0前置，2后置，因此一次遍历可得
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                # 0前置，指针右移
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2:
                # 2后置，指针不动，待排序长度-1
                nums.pop(i)
                nums.append(2)
                n -= 1
            else:
                # 1不动，指针右移
                i += 1


if __name__ == "__main__":
    s = Solution()
    s.sortColors2(case2)
    print(case2)

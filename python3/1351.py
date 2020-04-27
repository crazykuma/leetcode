""" 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 

请你统计并返回 grid 中 负数 的数目。

 

示例 1：

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。
示例 2：

输入：grid = [[3,2],[1,0]]
输出：0
示例 3：

输入：grid = [[1,-1],[-1,-1]]
输出：3
示例 4：

输入：grid = [[-1]]
输出：1
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

 """

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 二分算法，找每一行中大于0的那个最小值所在索引
        res=0

        for array in grid:
            l,r=0,len(array)-1
            while l<r:
                mid=(l+r)//2
                if array[mid]>=0:
                    l=mid+1
                else:
                    r=mid

            # l==r=mid+1
            if array[l]<0:
                res+=len(array)-l
        
        return res


if __name__ == "__main__":
    s=Solution()
    print(s.countNegatives([[1,-1],[-1,-1]]))
    print(s.countNegatives([[3,2],[1,0]]))


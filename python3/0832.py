""" 输入: [[1,1,0],[1,0,1],[0,0,0]]
输出: [[1,0,0],[0,1,0],[1,1,1]]
解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
 """
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        tmp = [array[::-1] for array in A]

        for array in tmp:
            for i in range(len(array)):
                array[i] = abs(1-array[i])

        return tmp

if __name__ == "__main__":
    s=Solution()
    assert s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])==[[1,0,0],[0,1,0],[1,1,1]]
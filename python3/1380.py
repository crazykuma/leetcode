from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # 两种方法可以生成列，注意zip方法和*传参
        minrow = [min(i) for i in matrix]
        # maxcol = [max([arr[col] for arr in matrix])
        #           for col in range(len(matrix[0]))]
        maxcol = [max(i) for i in zip(*matrix)]
        return [i for i in minrow if i in maxcol]


if __name__ == "__main__":
    s = Solution()
    print(s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
    print(s.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))

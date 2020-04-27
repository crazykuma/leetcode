from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        grid = [[0] * m for _ in range(n)]
        for x, y in indices:
            for i in range(m):
                grid[x][i] += 1
            for i in range(n):
                grid[i][y] += 1

        odds = 0
        for array in grid:
            odds += sum([n % 2 for n in array])

        return odds


    def oddCells2(self, n: int, m: int, indices: List[List[int]]) -> int:
        row=[0]*n
        col=[0]*m

        for x,y in indices:
            row[x]+=1
            col[y]+=1

        # 现在各行与各列的计数次数有了
        cnt_row=sum(i%2 for i in row) # 奇数次数的行
        cnt_col=sum(i%2 for i in col) # 奇数次数的列
        cnt_even_row=n-cnt_row        # 偶数次数的行
        cnt_even_col=m-cnt_col        # 偶数次数的列
        return cnt_row*cnt_even_col+cnt_col*cnt_even_row
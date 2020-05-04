from typing import List
case1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

case2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


class Solution:

    def isvalidRow(self, row: List[str]) -> bool:
        # 检验行是否有重复
        arr = [0]*10
        for s in row:
            if s != '.':
                arr[int(s)] += 1
                if arr[int(s)] > 1:
                    return False
        return True

    def isvalidCol(self, col: List[str]) -> bool:
        # 检验列是否有重复
        return self.isvalidRow(col)

    def isvalidCube(self, cube: List[List[str]]) -> bool:
        # 检验子数独是否有重复
        res = []
        for row in cube:
            for s in row:
                res.append(s)

        return self.isvalidRow(res)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 检验数独是否有效

        for row in board:
            if not self.isvalidRow(row):
                return False

        Tboard = [[arr[i] for arr in board] for i in range(len(board[0]))]
        for col in Tboard:
            if not self.isvalidCol(col):
                return False

        cubes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cube = [arr[j:j+3] for arr in board[i:i+3]]
                cubes.append(cube)

        for cube in cubes:
            if not self.isvalidCube(cube):
                return False

        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        # 参考题解后解法 一次遍历
        # 初始化数组
        Rows = [[0]*10 for i in range(9)]
        Cols = [[0]*10 for i in range(9)]
        Cubes = [[0]*10 for i in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                # i行，j列，(i//3)*3+j//3号cube
                n = int(board[i][j])
                Cube_idx = (i//3)*3+j//3
                if Rows[i][n] or Cols[j][n] or Cubes[Cube_idx][n]:
                    return False
                Rows[i][n] += 1
                Cols[j][n] += 1
                Cubes[Cube_idx][n] += 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku2(case1))
    print(s.isValidSudoku2(case2))

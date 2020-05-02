from typing import List
case1 = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        i_r = 0
        i_c = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    i_r = i
                    i_c = j
                    break

        # 横向
        row = board[i_r]
        col = [board[i][i_c] for i in range(len(board))]
        Srow = ''.join(row).replace('.', '')
        Scol = ''.join(col).replace('.', '')
        count_r = Srow.count('Rp')+Srow.count('pR')
        count_c = Scol.count('Rp')+Scol.count('pR')
        return count_c+count_r


if __name__ == "__main__":
    s = Solution()
    print(s.numRookCaptures(case1))

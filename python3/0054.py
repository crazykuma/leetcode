from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 笨办法，通过限制边界来实现
        if not matrix:
            return []
        else:
            m = len(matrix)
            n = len(matrix[0])
            x = 0
            y = 0
            top = 0
            bottom = m
            left = 0
            right = n
            res = []
            res.append(matrix[top][left])
            for i in range(m*n):
                if x == top and y < right-1:
                    # 右移
                    y += 1
                    res.append(matrix[x][y])
                    # 右移最后一步到y==n-1时，更新top+=1
                    if y == right-1:
                        top += 1
                    # x=top,x=bottom-1即只有此行未遍历，那每遍历一次左边界便缩小1次
                    if x == bottom-1:
                        left += 1
                elif y == right-1 and x < bottom-1:
                    # 下移
                    x += 1
                    res.append(matrix[x][y])
                    if x == bottom-1:
                        right -= 1
                    if y == left:
                        top += 1
                elif x == bottom-1 and y > left:
                    # 左移
                    y -= 1
                    res.append(matrix[x][y])
                    if y == left:
                        bottom -= 1
                    if x == top:
                        right -= 1
                elif y == left and x > top:
                    # 上移
                    x -= 1
                    res.append(matrix[x][y])
                    if x == top:
                        left += 1
                    if y == right-1:
                        bottom -= 1
            return res


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

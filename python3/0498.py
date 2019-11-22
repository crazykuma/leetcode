from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        else:
            m=len(matrix)
            n=len(matrix[0])
            x=0
            y=0
            result=[]
            for i in range(m+n-1):
                if i%2==0:
                    # 偶数行
                    while True:
                        result.append(matrix[x][y])
                        if (x==0 and y<n-1):
                            # 向上到顶但是没有到右边界，右移
                            y+=1
                            break
                        elif (y==n-1):
                            # 到右边界,下移
                            x+=1
                            break
                        else:
                            # 移动中
                            x-=1
                            y+=1
                else:
                    # 奇数行
                    while True:
                        result.append(matrix[x][y])
                        if (y==0 and x<m-1):
                            # 向下到左边界但是没有到底，下移
                            x+=1
                            break
                        elif (x==m-1):
                            # 向下到底，右移
                            y+=1
                            break
                        else:
                            # 移动中
                            x+=1
                            y-=1
        return result

if __name__ == "__main__":
    s=Solution()
    print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.findDiagonalOrder([[1,2],[3,4],[5,6]]))
    print(s.findDiagonalOrder([[1,2,3,4],[5,6,7,8]]))
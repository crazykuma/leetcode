from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 下一行的前n-1个数都是上一行的数相加而来
        # 下一行又比上一行多一个数
        # 因此在前一位加入一个0就是下一行数的个数
        # 然后对前n-1个数（此处还是上一行的数据）相加得到下一行的数据
        rowList = [1]
        for i in range(1, rowIndex+1):
            rowList.insert(0, 0)
            for j in range(i):
                rowList[j] = rowList[j]+rowList[j+1]
        return rowList


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(1))
    print(s.getRow(2))
    print(s.getRow(3))
    print(s.getRow(4))
    print(s.getRow(5))
    print(s.getRow(6))

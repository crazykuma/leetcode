from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 此题矩形左上角坐标为（x1,y2)左下角为(x1,y1),右上角为(x2,y2)右下角为(x2,y1)
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x11, y11, x22, y22 = rec2[0], rec2[1], rec2[2], rec2[3]
        # 反向思考，如果要让两矩形不重叠，那么有4种情况，即在矩形1的上下左右4周
        case1 = x11 >= x2  # right
        case2 = y11 >= y2  # upper
        case3 = x22 <= x1  # left
        case4 = y22 <= y1  # bottom
        return not (case1 or case2 or case3 or case4)


if __name__ == "__main__":
    s = Solution()
    assert s.isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]) == True
    assert s.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]) == False

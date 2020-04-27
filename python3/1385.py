from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for x in arr1:
            cnt = all(abs(x-y) > d for y in arr2)
            # tips: all函数当所有迭代器返回都为真时，返回真，否则有一个假就返回假
            count += cnt

        return count

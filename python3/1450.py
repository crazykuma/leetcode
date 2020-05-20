from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return [1 for s, e in zip(startTime, endTime) if s <= queryTime <= e].count(1)


if __name__ == "__main__":
    s = Solution()
    print(s.busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))

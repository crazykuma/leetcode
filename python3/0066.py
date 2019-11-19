from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ori = 0
        for i in range(len(digits)):
            ori = ori*10+digits[i]
        return [int(i) for i in str(ori+1)]


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))

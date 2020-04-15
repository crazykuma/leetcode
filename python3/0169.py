from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0)+1

        l = len(nums)
        for k, v in d.items():
            if v > l/2:
                return k


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))  # 3

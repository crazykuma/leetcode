from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 使用内建函数sort()
        for i in range(n):
            nums1[m+i] = nums2[i]

        nums1.sort()
        return nums1


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

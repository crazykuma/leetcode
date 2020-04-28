from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # 线性搜索
        left = 0
        while A[left] < A[left+1]:
            left += 1

        return left

    def peakIndexInMountainArray2(self, A: List[int]) -> int:
        # 二分查找
        low, high = 0, len(A)-1
        while low < high:
            mid = (low+high)//2
            # 上坡处
            if A[mid-1] < A[mid] < A[mid+1]:
                low = mid+1
            # 下坡处
            elif A[mid+1] < A[mid] < A[mid-1]:
                high = mid-1
            else:
                return mid
        return low

    def peakIndexInMountainArray3(self, A: List[int]) -> int:
        # index,max
        return A.index(max(A))


if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray([0, 1, 0]))
    print(s.peakIndexInMountainArray2([18, 29, 38, 59, 98, 100, 99, 98, 90]))
    print(s.peakIndexInMountainArray3([18, 29, 38, 59, 98, 100, 99, 98, 90]))

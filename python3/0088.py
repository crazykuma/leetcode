from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 使用内建函数sort() 48ms
        for i in range(n):
            nums1[m+i] = nums2[i]

        nums1.sort()
        return nums1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 归并排序 64ms
        tmp = nums1[:m]  # copy nums1
        i = 0
        j = 0
        k = 0
        while(i < m and j < n):
            if(tmp[i] < nums2[j]):
                nums1[k] = tmp[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        
        while(i < m):
            nums1[k] = tmp[i]
            k += 1
            i += 1

        while(j < n):
            nums1[k] = nums2[j]
            k += 1
            j += 1

        return nums1


if __name__ == "__main__":
    s = Solution()
    print(s.merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

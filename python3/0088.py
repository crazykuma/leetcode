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

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前排序
        i = m+n-1
        pos_A = m-1
        pos_B = n-1
        while pos_A > -1 and pos_B > -1:
            # 比较A和B的最后两个数
            if nums1[pos_A] >= nums2[pos_B]:
                nums1[i] = nums1[pos_A]
                i -= 1
                pos_A -= 1
            else:
                nums1[i] = nums2[pos_B]
                pos_B -= 1
                i -= 1
        # 当A已经排完而B还有数字
        # 把B的剩余数字往A前面填
        while pos_B > -1:
            nums1[pos_B] = nums2[pos_B]
            pos_B -= 1
        return nums1


if __name__ == "__main__":
    s = Solution()
    print(s.merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

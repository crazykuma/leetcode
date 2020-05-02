from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = nums1 if len(nums1) < len(nums2) else nums2
        n2 = nums2 if len(nums1) < len(nums2) else nums1
        ans = []
        for i in n1:
            if i in n2:
                ans.append(i)
                n2.remove(i)
        return ans

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 增加字典方法，对出现次数进行计数
        d = dict()
        for n in nums1:
            d[n] = d.get(n, 0)+1

        res = []
        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                d[n] -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(s.intersect([1, 2, 2, 1], [2]))
    print(s.intersect([3, 1, 2], [1, 1]))  # [1]

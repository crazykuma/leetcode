from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = nums1 if len(nums1) < len(nums2) else nums2
        n2 = nums2 if len(nums1) < len(nums2) else nums1
        ans=[]
        for i in n1:
            if i in n2:
                ans.append(i)
                n2.remove(i) 
        return ans


if __name__ == "__main__":
    s=Solution()
    print(s.intersect([1,2,2,1],[2,2]))
    print(s.intersect([4,9,5],[9,4,9,8,4]))
    print(s.intersect([1,2,2,1],[2]))
    print(s.intersect([3,1,2],[1,1])) # [1]
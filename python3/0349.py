from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [i for i in set(nums1) if i in set(nums2)]

if __name__ == "__main__":
    s=Solution()
    print(s.intersection([1,2,2,1],[2,2]))  # [2]
    print(s.intersection([4,9,5],[9,4,9,8,4])) #[9,4]


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while(i < n-1):
            if(nums[i] == nums[i+1]):
                nums.pop(i+1)
            else:
                i += 1
            n = len(nums)
        print(nums)
        return n

    def removeDuplicates2(self, nums: List[int]) -> int:
        # 集合：通用框架
        i = 0
        n = len(nums)
        d = set()
        while i < n:
            if nums[i] not in d:
                d.add(nums[i])
                i += 1
            else:
                nums.pop(i)
                n -= 1
        print(nums)
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))

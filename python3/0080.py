from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 通用框架：字典
        d = dict()
        i = 0
        n = len(nums)
        while i < n:
            if d.get(nums[i], 0) < 2:
                d[nums[i]] = d.get(nums[i], 0)+1
                i += 1
            else:
                nums.pop(i)
                n -= 1

        print(nums)       # 验证之用，提交时注释
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))

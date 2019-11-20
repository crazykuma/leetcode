from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 要使长度为2n的数据分为n组
        # 取n组min(a,b)的和最大
        # 即ab之差尽可能小，那么排序后直接取奇数位的和即可得
        nums=sorted(nums)
        return sum(nums[::2])

if __name__ == "__main__":
    s=Solution()
    print(s.arrayPairSum([1,4,3,2]))
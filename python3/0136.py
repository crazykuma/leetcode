from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i, n in enumerate(nums):
            if d.get(n, 0):
                # 存在
                d.pop(n)
            else:
                # 不存在
                d[n] = i

        return d.popitem()[0]

    def singleNumber2(self, nums: List[int]) -> int:
        # 异或
        # a^a=0所以出现两次的数都会被消除
        # 0^a=a所以最后留下出现一次的数就是a
        a = 0
        for n in nums:
            a = a ^ n
        return a


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber2([4, 1, 2, 1, 2]))

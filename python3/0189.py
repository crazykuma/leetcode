from typing import List
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1 pop,insert方法 164ms
        # 向右移动k个位置，即把后k位数提前
        for i in range(k):
            nums.insert(0,nums.pop())
        return nums

    def rotate2(self, nums:List[int],k:int)-> None:
        # 2 84ms
        # 还是把后k位数提前
        # 因为后k位数顺序不变
        # 因此可以分为两块数据[:n-k]和[n-k:]
        # 考虑k>n的情况，因为当k=n时，可以看作移动0个位置
        # 因此有k=k%n取余
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k:]+nums[:n-k]
        return nums

if __name__ == "__main__":
    s=Solution()
    print(s.rotate([1,2],k=3))
    print(s.rotate2([1,2,3,4,5,6,7],k=3))

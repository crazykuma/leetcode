from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 插入排序的尾排序
        # 输入: [0,1,0,3,12]
        # 输出: [1,3,12,0,0]
        # 可以用append和pop来完成,这两个操作都是O(1)的
        i=0
        n=len(nums)
        while i < n:
            if nums[i]==0:
                num=nums.pop(i)
                nums.append(num)
                n=n-1
            else:
                i+=1
        return nums


if __name__ == "__main__":
    s=Solution()
    print(s.moveZeroes([0,1,0,3,0,12,0,0,1]))
    print(s.moveZeroes([0,1,0,3,12]))
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def leftbound(nums, target):
            # 查找左侧边界,左闭右开
            if not nums:
                return -1
            l = 0
            r = len(nums)  # 左闭右开
            while l < r:  # 左闭右开，所以是<
                mid = (l+r) >> 1
                if nums[mid] >= target:
                    # 缩小右边界
                    # 为什么=也要用在这里？
                    # 1.当前找到的这个值左边可能还有这个值，因此我们继续向左查找
                    r = mid  # 左闭右开，所以mid不用-1
                else:
                    # nums[mid]<target
                    l = mid+1  # 左闭右开，左边mid已经搜索过，所以+1

            # l==r
            # 1. 找到target：l=r=mid
            # 2. 没找到target:
            #   2.1 target位于区间内：l=r=mid,nums[l]!=target
            #   2.2 target位于区间外：l不可能比0小，l最大会等于len(nums)
            if l == len(nums):
                return -1
            return l if nums[l] == target else -1

        def leftbound2(nums, target):
            # 查找左侧边界，左右都闭
            if not nums:
                return -1

            l = 0
            r = len(nums)-1  # 条件更改
            while l <= r:  # 条件更改
                mid = (l+r) >> 1
                if nums[mid] >= target:
                    # 缩小右边界
                    # mid已经搜索过
                    r = mid-1
                else:
                    # nums[mid]<target
                    # 缩小左边界
                    l = mid+1
            # l=r+1
            # 1. 已经找到target，此时l=r+1=mid,返回l的值
            # 2. 没有找到target, 此时l最小是0，最大则会走出索引边界到len(nums)
            # if l>=len(nums) or nums[l]!=target:
            #     return -1
            # return l
            # 次数or的前后顺序不能换，否则会数组越界
            return -1 if (l >= len(nums or nums[l] != target)) else l

        def rightbound(nums, target):
            # 查找右侧边界，左闭右开
            if not nums:
                return -1
            l = 0
            r = len(nums)
            while l < r:
                mid = (l+r) >> 1
                if nums[mid] == target:
                    # 当前右边可能还有这个值，因此继续向左
                    # 左闭右开
                    l = mid+1
                if nums[mid] < target:
                    # 向右查找
                    l = mid+1
                if nums[mid] > target:
                    # 向左查找
                    r = mid

            # l==r时跳出
            # 1. 找到target：l=mid+1=r,返回l-1或者r-1
            # 2. 没找到target：l==r,因为是查找右边界，右侧不断缩减，所以r==0==l时跳出
            if l == 0:
                return -1
            return l-1 if nums[l-1] == target else -1

        def rightbound2(nums, target):
            # 查找右侧边界，左右都闭
            if not nums:
                return -1
            l = 0
            r = len(nums)-1
            while l <= r:
                mid = (l+r) >> 1
                if nums[mid] <= target:
                    l = mid+1
                else:
                    r = mid-1

            # l=r+1时跳出
            # 1. 找到target,l=mid+1=r+1,返回l-1
            # 2. 没有找到target,同样要考虑数组越界的问题
            # 查找右侧边界，当右侧一直找不到时，r会走到索引0前面
            return -1 if (r < 0 or nums[r] != target) else r

        l = leftbound(nums, target)
        r = rightbound(nums, target)
        return [l, r]


if __name__ == "__main__":
    s = Solution()

    assert s.searchRange([2, 2], 3) == [-1, -1]
    assert s.searchRange([2, 2], 0) == [-1, -1]
    assert s.searchRange([7, 7, 8, 8, 10], 7) == [0, 1]
    assert s.searchRange([3, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([1], 8) == [-1, -1]
    assert s.searchRange([], 1) == [-1, -1]
    assert s.searchRange([1], 1) == [0, 0]
    assert s.searchRange([1], 2) == [-1, -1]
    assert s.searchRange([2, 2], 2) == [0, 1]

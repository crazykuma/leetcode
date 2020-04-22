# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n: int, k: int) -> int:
        """
        :type n: int range n
        :type k: int target bad version
        :rtype: int
        """
        target = k

        def isBadVersion(v):
            if v >= target:
                return True
            else:
                return False
        # 二分查找
        left = 1
        right = n
        while left <= right:
            mid = (left+right)//2
            re = isBadVersion(mid)
            if re:
                # true，版本错误，更新右边界
                right = mid-1
            else:
                # false, 版本正确，更新左边界
                left = mid+1

        return left


if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(1, 1))
    print(s.firstBadVersion(2, 2))
    print(s.firstBadVersion(3, 2))

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 双指针
        pl = 0
        pr = len(A)-1
        total = sum(A)
        if total % 3 != 0:
            return False
        target = total//3
        left_sum = A[pl]
        right_sum = A[pr]
        while pl+1 < pr:
            if left_sum == right_sum == target:
                return True
            if left_sum != target:
                pl += 1
                left_sum += A[pl]
            if right_sum != target:
                pr -= 1
                right_sum += A[pr]

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10]))
    print(s.canThreePartsEqualSum([1, -1, 1, -1]))

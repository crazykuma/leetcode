from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        TA = [[arr[i] for arr in A] for i in range(len(A[0]))]
        count = 0
        for arr in TA:
            if arr != sorted(arr):
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.minDeletionSize(["cba", "daf", "ghi"]) == 1

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        max_val = max(A)
        loc = A.index(max_val)
        # 分成两截
        if loc == n-1 or loc == 0:
            return False
        i = 0
        j = loc
        while i < loc:
            if A[i] >= A[i+1]:
                return False
            i += 1

        while j < n-1:
            if A[j] <= A[j+1]:
                return False
            j += 1

        return True

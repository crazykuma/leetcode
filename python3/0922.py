from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0]*len(A)
        odd_idx = 1
        even_idx = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                res[even_idx] = A[i]
                even_idx += 2
            else:
                res[odd_idx] = A[i]
                odd_idx += 2

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParityII([4, 2, 5, 7]))

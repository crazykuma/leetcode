from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # 此法更快一点
        return [[arr[j] for arr in A] for j in range(len(A[0]))]

    def transpose2(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))


if __name__ == "__main__":
    s = Solution()
    print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.transpose2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

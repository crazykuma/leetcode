from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        total_list = []
        for i in range(1, numRows+1):
            sub_list = [1 for i in range(i)]
            if i > 2:
                for n in range(1, i-1):
                    left = total_list[i-2][n-1]
                    right = total_list[i-2][n]
                    sub_list[n] = left+right
            total_list.append(sub_list)
        return total_list


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))

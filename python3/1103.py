from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 暴力法
        ans = [0]*num_people
        i = 0
        while candies > 0:
            if candies > i:
                ans[i % num_people] += i+1
                candies -= (i+1)
            else:
                ans[i % num_people] += candies
                candies -= candies
            i += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies(7, 4))
    print(s.distributeCandies(10, 3))

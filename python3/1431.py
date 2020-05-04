from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = [0]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandy:
                res[i] = True
            else:
                res[i] = False

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))

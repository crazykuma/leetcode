from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            d[n] = d.get(n, 0)+1

        res = [k for k, v in d.items() if k == v]

        return max(res) if res else -1


if __name__ == "__main__":
    s = Solution()
    assert s.findLucky([2, 2, 3, 4]) == 2
    assert s.findLucky([1, 2, 2, 3, 3, 3]) == 3

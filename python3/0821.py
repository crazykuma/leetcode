from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        idxs = [i for i, n in enumerate(S) if n == C]
        res = []
        for i, char in enumerate(S):
            distance = [abs(i-k) for k in idxs]
            res.append(min(distance))

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.shortestToChar(S="loveleetcode", C='e') == [
        3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        score = 0
        for op in ops:
            if op == '+':
                score = score+scores[-2]+scores[-1]
                scores.append(scores[-2]+scores[-1])
            elif op == 'D':
                score = score+2*scores[-1]
                scores.append(2*scores[-1])
            elif op == 'C':
                score -= scores[-1]
                scores.pop()
            else:
                score += int(op)
                scores.append(int(op))

        return score


if __name__ == "__main__":
    s = Solution()
    assert s.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27

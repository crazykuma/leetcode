class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 用后进先出的栈
        stack = []
        d = {"L": "R", "R": "L"}
        count = 0
        for c in s:
            if not stack:
                stack.append(c)
            elif c == stack[-1]:
                # 相同则继续放入
                stack.append(c)
            elif c != stack[-1] and stack[-1] == d[c]:
                # 成对则取出
                stack.pop()
            if len(stack) == 0:
                # 栈为空时计数+1
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.balancedStringSplit("RLRRLLRLRL") == 4
    assert s.balancedStringSplit("RLLLLRRRLR") == 3

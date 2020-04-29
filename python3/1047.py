class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 栈的思路，将相邻的都成对消除，剩下的就是要求的字符串
        stack = []
        for c in S:
            if not stack or c != stack[-1]:
                stack.append(c)
            elif c == stack[-1]:
                stack.pop()

        return ''.join(stack)

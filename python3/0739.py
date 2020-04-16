from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 从前往后遍历
        stack = []
        n = len(T)
        res = [0]*n
        for i in range(n):
            # 栈存的是值的下标
            # 如果新值大于栈顶，则出栈，并标记
            while stack and T[i] > T[stack[-1]]:
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)

        return res



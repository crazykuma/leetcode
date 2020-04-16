from typing import List


class Solution:
    """
    逆波兰表达式求值

    """

    def evalRPN(self, tokens: List[str]) -> int:
        # 根据逆波兰表达式的定义，可分为参数a,参数b，运算符op三个部分。
        # 使用栈的思想，将非运算符的部分按顺序压入栈。
        # 根据得到的运算符，从栈中提取参数a和参数b，然后将计算结果压入栈中。
        # 最后栈中只剩一个元素，就是要求的值。
        stack = []
        op = ["+", "-", "*", "/"]
        for c in tokens:
            if c not in op:
                stack.append(c)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(eval("{}{}{}".format(b, c, a)))

        return int(stack[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11",
                     "*", "/", "*", "17", "+", "5", "+"]))  # 22
    print(s.evalRPN(["4", "13", "5", "/", "+"]))  # 6
    print(s.evalRPN(["18"]))  # 18

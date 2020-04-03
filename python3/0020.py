"""
学习栈的概念。
使用list来实现栈的后进先出功能LIFO
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 注意空字符串可被认为是有效字符串。
        d = {"(": ")", "{": "}", "[": "]"}
        stack=[]
        for c in s:
            if c in d:
                stack.append(c)
            else:
                # 不是左括号，则是右括号
                # 此时判断栈顶是否是对应的左括号
                if stack  and c == d.get(stack[-1]):
                    # 如果是，那么从栈顶取出元素
                    stack.pop()
                else:
                    # 如果不是，则说明闭合顺序出了问题
                    return False
        return len(stack)==0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))     # False
    print(s.isValid("([)]"))   # False
    print(s.isValid("{[]}"))   # True
    print(s.isValid("()()"))   # True
    print(s.isValid("]"))      # False
    print(s.isValid("([]"))    # False
    print(s.isValid("[])"))    # False

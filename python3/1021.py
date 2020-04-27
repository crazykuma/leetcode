class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        res=''
        for c in S:
            if c=="(":
                stack.append(c)
                if len(stack)>1:
                    # 有（，后面添加的是原语
                    res+=c
            else:
                stack.pop()
                if len(stack)>0:
                    res+=c

        return res


if __name__ == "__main__":
    s=Solution()
    assert s.removeOuterParentheses("(()())(())")=="()()()"
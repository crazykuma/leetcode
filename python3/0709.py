class Solution:
    def toLowerCase(self, str: str) -> str:
        res=''
        for c in str:
            if c.islower():
                res+=c
            else:
                res+=c.lower()

        return res

    def toLowerCase2(self,str:str)->str:
        return str.lower()

    def toLowerCase3(self,str:str)->str:
        return ''.join([c.lower() for c in str])


if __name__ == "__main__":
    s=Solution()
    assert s.toLowerCase('Hello')=='hello'
    assert s.toLowerCase2('Hello')=='hello'
    assert s.toLowerCase3('Hello')=='hello'

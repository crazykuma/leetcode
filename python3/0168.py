class Solution:
    def convertToTitle(self, n: int) -> str:
        s="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #0-25
        res=""
        while n>26:
            i=n%26
            n=n//26
            if i==0: # 退位
                n=n-1
            res+=s[i-1]
        else:
            res+=s[n-1]

        return res[::-1]

if __name__ == "__main__":
    s=Solution()
    print(s.convertToTitle(1))
    print(s.convertToTitle(26))
    print(s.convertToTitle(27))
    print(s.convertToTitle(28))
    print(s.convertToTitle(701))
    print(s.convertToTitle(52))
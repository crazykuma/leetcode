from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        c=0
        if x>0:
            symbol=1
        else:
            symbol=-1
        x=abs(x)
        while(x>0):
            a=x%10
            x//=10
            c=c*10+a
        if c<=2**31-1 and c>=-2**31:
            return c*symbol
        else:
            return 0


if __name__ == "__main__":
    s=Solution()
    print(s.reverse(120))
    print(s.reverse(-123))
    print(s.reverse(123))
    print(s.reverse(7463847413))
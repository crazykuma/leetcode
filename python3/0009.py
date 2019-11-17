from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=0
        ori=x
        if x<0:
            return False
        else:
            while(x):
                a=x%10
                x//=10
                c=c*10+a
            if ori==c:
                return True
            else:
                return False

if __name__ == "__main__":
    s=Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            # s[i],s[j]=s[j],s[i] 
            tmp=s[i]
            s[i]=s[j]
            s[j]=tmp
            i+=1
            j-=1
        return s

if __name__ == "__main__":
    s=Solution()
    print(s.reverseString(["h","e","l","l","o"]))
    print(s.reverseString(["a","p","p","l","e"]))
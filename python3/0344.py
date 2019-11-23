from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 使用双指针
        i = 0
        j = len(s)-1
        while i < j:
            s[i],s[j]=s[j],s[i]
            i += 1
            j -= 1
        return s  # 这行不用提交

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 要求使用递归,提交后内存溢出
        def recur(ss: List[str]) -> List:
            if len(ss) <= 1:
                return ss
            else:
                return recur(ss[1:])+[ss[0]]
        s[:] = recur(s)
        return s  #这行不用提交

    def reverseString3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 使用递归+双指针
        def recur(ss:List[str],i:int,j:int)->List:
            if i>j:
                return
            else:
                ss[i],ss[j]=ss[j],ss[i]
                return recur(ss,i+1,j-1)
        recur(s,0,len(s)-1)
        return s #这行不用提交


if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(["h", "e", "l", "l", "o"]))
    print(s.reverseString2(["h", "e", "l", "l", "o"]))
    print(s.reverseString3(["h", "e", "l", "l", "o"]))

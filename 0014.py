from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        n=len(strs)
        if n==0:
            return ""
        if not strs[0]:
            return strs[0]
        for i in range(len(strs[0])):
            prefix+=strs[0][i]
            newlist=[1 if stri.startswith(prefix) else 0 for stri in strs]
            if sum(newlist)==n:
                if i==len(strs[0])-1:
                    return prefix
                else:
                    continue
            else:
                return prefix[:-1]

if __name__ == "__main__":
    s=Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["aa","aa"]))
    print(s.longestCommonPrefix(["cat"]))


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:return -1
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for k,v in d.items():
            if v==1:
                return s.index(k)
        else:
            return -1

if __name__ == "__main__":
    s=Solution()
    print(s.firstUniqChar("cccaabadb"))
    print(s.firstUniqChar(""))
    print(s.firstUniqChar("leetcode"))


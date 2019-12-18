class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds={}
        dt={}
        for c in s:
            ds[c]=ds.get(c,0)+1
        
        for c in t:
            dt[c]=dt.get(c,0)+1

        if ds==dt:
            return True
        else:
            return False


if __name__ == "__main__":
    s=Solution()
    print(s.isAnagram("rat","car")) # False
    print(s.isAnagram("",""))       # True
    print(s.isAnagram("a","ab"))    # False
    print(s.isAnagram("aacc","ccac")) # False
    print(s.isAnagram("anagram","nagaram")) # True
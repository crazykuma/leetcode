class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1



if __name__ == "__main__":
    s=Solution()
    print(s.strStr(haystack="hello",needle="ll"))
    print(s.strStr(haystack="aaaaa",needle="bba"))

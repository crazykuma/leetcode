class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        if words:
            return len(words[-1])
        else:
            return 0

if __name__ == "__main__":
    s=Solution()
    print(s.lengthOfLastWord(" "))
    print(s.lengthOfLastWord("Hello world Python"))
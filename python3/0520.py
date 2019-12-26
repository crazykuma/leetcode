class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n=len(word)
        c=0
        for e in word:
            if e.isupper():
                c+=1
        if c==n:
            return True
        elif c==0:
            return True
        elif c==1:
            if word[0].isupper():
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    s=Solution()
    print(s.detectCapitalUse("USA"))
    print(s.detectCapitalUse("Google"))
    print(s.detectCapitalUse("leetcode"))
    print(s.detectCapitalUse("FlaG"))

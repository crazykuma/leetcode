class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 去空格标点符号
        # 转换为小写
        s=''.join(e.lower() for e in s if e.isalnum())
        t=s[::-1]
        if t==s:
            return True
        else:
            return False


if __name__ == "__main__":
    s=Solution()
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome("A man, a plan, a canal:Panama"))

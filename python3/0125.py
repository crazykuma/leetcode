class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 去空格标点符号
        # 转换为小写
        s = ''.join(e.lower() for e in s if e.isalnum())
        t = s[::-1]
        if t == s:
            return True
        else:
            return False

    def isPalindrome2(self, s: str) -> bool:
        # 双指针写法
        # 首先去除非字母和数字字符
        s = ''.join([i.lower() for i in s if i.isalnum()])
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome2("race a car") == False
    assert s.isPalindrome2("A man, a plan, a canal:Panama") == True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            # s为空时是任何字符串的子集
            return True
        if len(set(s)-set(t)) > 0:
            # s与t的差异不为空时，s不是任何t的子集
            return False
        i, j = 0, 0
        m, n = len(s), len(t)
        cur = ''
        while i < m and j < n:
            # 判断字符串t的值是否是下一个字符串s的值
            if t[j] != s[i]:
                j += 1
            else:
                cur += t[j]
                if s == cur:
                    return True
                i += 1
                j += 1

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.isSubsequence("", "ahbgdc") == True
    assert s.isSubsequence("abc", "ahbgdc") == True
    assert s.isSubsequence("axc", "ahbgdc") == False

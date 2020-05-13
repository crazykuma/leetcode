class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口法
        if not s:
            return 0
        d = set()
        maxleng = 0
        n = len(s)
        i = j = 0
        while i <= j < n:
            if s[j] not in d:
                # 扩大窗口
                d.add(s[j])
                maxleng = max(maxleng, j-i+1)
                j += 1
            else:
                # 缩小窗口
                d.discard(s[i])
                i += 1

        return maxleng


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))

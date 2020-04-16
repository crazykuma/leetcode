class Solution:
    # 单词规律，和同构字符串的0205题完全一样
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        used = []
        t = str.split()
        if len(pattern) != len(t):
            return False
        n = len(pattern)
        for i in range(n):
            if pattern[i] in d and t[i] != d[pattern[i]]:
                # aa,ab
                return False
            if pattern[i] not in d and t[i] in used:
                # ab,aa
                return False
            d[pattern[i]] = t[i]
            used.append(t[i])
        return True

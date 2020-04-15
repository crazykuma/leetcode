class Solution:
    """同构字符串
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # 长度不同则False
        n = len(s)
        d = {}
        used = []
        for i in range(n):
            if s[i] in d and t[i] != d[s[i]]:
                # 当d[s[i]]和t[i]不等，有aa,ab的映射
                return False
            if s[i] not in d and t[i] in used:
                # 当s[i]未使用而t[i]已经使用，有ab,aa映射
                return False
            d[s[i]] = t[i]
            used.append(t[i])

        return True

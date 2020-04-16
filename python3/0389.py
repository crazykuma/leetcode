"""给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 哈希表
        d = {}
        for c in s:
            d[c] = d.get(c, 0)+1
        for c in t:
            d[c] = d.get(c, 0)-1
            if d[c] < 0:
                return c

    def findTheDifference2(self, s: str, t: str) -> str:
        # ASCII码
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
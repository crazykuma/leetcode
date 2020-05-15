class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 集合的差集和交集用法
        ransomSet = set(ransomNote)
        magSet = set(magazine)
        # 赎金信与杂志字符的差集大于0，则缺少字符，返回False
        if len(ransomSet-magSet) > 0:
            return False
        # 赎金信与杂志字符的交集字符中，赎金信中的特定字符数量多于杂志，返回False
        intersection = ransomSet and magSet
        for key in intersection:
            if ransomNote.count(key) > magazine.count(key):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True

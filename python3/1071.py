class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 递归法解
        # 假若两字符串存在最大公因子，则str1与str2都为某个str*N的长度，因此前后顺序可变
        if str1+str2 != str2+str1:
            return ""
        # 判断哪个字符串更长
        diff = len(str1)-len(str2)
        if diff > 0:
            # str1更长，则减去str1的str2长的部分
            str1 = str1[len(str2):]
        elif diff < 0:
            # str2更长，则减去str2的str1长的部分
            str2 = str2[len(str1):]
        else:
            # len(str1)==len(str2)
            return str1

        # 对剩下的str1,str2继续判断，直到得出结果
        return self.gcdOfStrings(str1, str2)


if __name__ == "__main__":
    s = Solution()
    assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert s.gcdOfStrings("LEET", "CODE") == ""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        # 反向遍历
        # 有#开头计算2个
        res = ''
        asc = ord('a')-1
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                res += chr(int(s[i-2:i])+asc)
                i -= 3
            else:
                res += chr(int(s[i])+asc)
                i -= 1

        return res[::-1]


if __name__ == "__main__":
    s=Solution()
    assert s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")=="abcdefghijklmnopqrstuvwxyz"
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        小数在大数前，小数由正转负，但考虑不存在 IC,ID,IM等情况，应限定范围防止错误
        """
        n = 0
        l = len(s)
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if l == 1:
            n = d.get(s)
            return n
        else:
            n = 0
            for i in range(l):
                if i < l-1:
                    if s[i] == "I" and s[i+1] in ["V", "X"]:
                        n += d.get(s[i])*(-1)
                    elif s[i] == "X" and s[i+1] in ["L", "C"]:
                        n += d.get(s[i])*(-1)
                    elif s[i] == "C" and s[i+1] in ["D", "M"]:
                        n += d.get(s[i])*(-1)
                    else:
                        n += d.get(s[i])
                else:
                    n += d.get(s[i])
            return n


if __name__ == "__main__":
    s = Solution()
    s.romanToInt("III")  # 1+1+1
    s.romanToInt("IV")  # 5-1
    s.romanToInt('IX')  # 10-1
    s.romanToInt('LVIII')  # 50+5+1+1+1
    s.romanToInt("MCMXCIV")  # 1000+(1000-100)+(100-10)+(5-4)

class Solution:
    def myAtoi(self, str: str) -> int:
        upLimit = pow(2, 31)-1
        lowLimit = pow(-2, 31)
        s = str.lstrip()
        if len(s) < 1:
            return 0

        if s[0] == '-':
            symbol = -1
            start = 1
        elif s[0] == '+':
            symbol = 1
            start = 1
        elif '0' <= s[0] <= '9':
            symbol = 1
            start = 0
        else:
            symbol = 0
            return 0

        num = 0
        for i in range(start, len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])
            else:
                break
        num = symbol*num
        if num > upLimit:
            return upLimit
        elif num < lowLimit:
            return lowLimit
        else:
            return num


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))  # 42
    print(s.myAtoi(""))   # 0
    print(s.myAtoi(" "))  # 0
    print(s.myAtoi("+1"))  # 1
    print(s.myAtoi("   -42"))  # -42
    print(s.myAtoi("4193 with 3 words"))  # 4193
    print(s.myAtoi("words and 987"))  # 0
    print(s.myAtoi("-91283472332"))  # -2147483648

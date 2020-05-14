class Solution:
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        # 注意：在py3.5之前的版本中字典是无序存放的
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                   90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for key in d:
            while num >= key:
                res += d[key]
                num -= key
        return res

    def intToRoman2(self, num: int) -> str:
        # 使用数组或者元组
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        res = ''
        for key, roman in d:
            while num >= key:
                res += roman
                num -= key
        return res


if __name__ == "__main__":
    s = Solution()
    assert (s.intToRoman2(3999)) == "MMMCMXCIX"
    assert (s.intToRoman2(1994)) == "MCMXCIV"

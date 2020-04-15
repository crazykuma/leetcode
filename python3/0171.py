class Solution:
    """Excel表列序号
    倒序后按26进位求和即可
    """
    def titleToNumber(self, s: str) -> int:
        f='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digi=0
        mi=0
        for char in s[::-1]:
            digi+=(f.index(char)+1)*pow(26,mi)
            mi+=1
        return digi
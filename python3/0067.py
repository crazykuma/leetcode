class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=eval('0b'+a)+eval('0b'+b)
        return bin(s)[2:]




if __name__ == "__main__":
    s=Solution()
    print(s.addBinary(a='11',b='1'))
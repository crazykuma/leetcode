
class Solution:
    def reverseWords(self, s: str) -> str:
        # 输入: "a good   example"
        # 输出: "example good a"
        # 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
        # 用split和join方法实现
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    s=Solution()
    print(s.reverseWords(s="the sky is blue"))
    print(s.reverseWords(s="  hello world!  "))
    print(s.reverseWords(s="a good   example"))
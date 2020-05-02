"""
有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。
给你一个数字 K，请你重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符；
而第一个分组中，至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。
给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。 """


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "")
        S = S.upper()
        res = ''
        j = 0
        for i in range(len(S)-1, -1, -1):
            if j < K:
                j += 1
            else:
                res += '-'
                j = 1
            res += S[i]

        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    assert s.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
    assert s.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J"

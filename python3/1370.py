""" 给你一个字符串 s ，请你根据下面的算法重新构造字符串：

1. 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
2. 从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
3. 重复步骤 2 ，直到你没法从 s 中选择字符。
4. 从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
5. 从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
6. 重复步骤 5 ，直到你没法从 s 中选择字符。
7. 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。

 

示例 1：

输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"

 """


class Solution:
    def sortString(self, s: str) -> str:
        # 首先将字符按照排序顺序存进数组中计数
        # 然后先从小到大选取，选中计数-1
        # 选完后从大到小选取，选中计数-1
        # 全部选完后返回得到的字符串
        res = ''
        arr = [0]*26
        total = 0
        for c in s:
            i = ord(c)-97
            arr[i] += 1
            total += 1

        while total > 0:
            for i in range(26):
                if arr[i] > 0:
                    res += chr(i+97)
                    arr[i] -= 1
                    total -= 1

            for i in range(25, -1, -1):
                if arr[i] > 0:
                    res += chr(i+97)
                    arr[i] -= 1
                    total -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.sortString("aaaabbbbcccc") == "abccbaabccba"

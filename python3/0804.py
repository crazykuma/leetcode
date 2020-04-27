""" 例如:
输入: words = ["gin", "zen", "gig", "msg"]
输出: 2
解释: 
各单词翻译如下:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

共有 2 种不同翻译, "--...-." 和 "--...--.".
 """
from typing import List
words = ["gin", "zen", "gig", "msg"]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                 "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        while words:
            res = ''
            word = words.pop()
            for c in word:
                res += morse[alpha.index(c)]

            if res not in d:
                d[res] = 1

        return len(d)


if __name__ == "__main__":
    s = Solution()
    assert s.uniqueMorseRepresentations(words) == 2

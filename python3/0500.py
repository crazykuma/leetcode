from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = 'qwertyuiop'
        line2 = 'asdfghjkl'
        line3 = 'zxcvbnm'
        res = []
        for word in words:
            tmp = word.lower()
            if tmp.strip(line1) == '' or tmp.strip(line2) == '' or tmp.strip(line3) == '':
                res.append(word)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))

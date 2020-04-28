from typing import List

words = ["cat", "bt", "hat", "tree"]
chars = "atach"


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        used_count = 0
        d_chars = {}
        for c in chars:
            d_chars[c] = d_chars.get(c, 0)+1

        for word in words:
            word_count = 0
            for c in word:
                if d_chars.get(c) and word.count(c) <= d_chars[c]:
                    word_count += 1
                else:
                    break
            if word_count == len(word):
                used_count += word_count

        return used_count


if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(words, chars))

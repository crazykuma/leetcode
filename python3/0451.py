class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict()
        for c in s:
            d[c] = d.get(c, 0)+1

        # 按照值的降序进行排列
        sd = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)

        res = ''
        for char, nums in sd:
            while nums > 0:
                res += char
                nums -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))

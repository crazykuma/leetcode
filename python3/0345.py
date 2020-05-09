class Solution:
    def reverseVowels(self, s: str) -> str:
        # 栈
        pool = 'aeiouAEIOU'
        arr = [0]*len(s)
        stack = []
        for i in range(len(s)):
            if s[i] not in pool:
                arr[i] = s[i]
            else:
                stack.append(s[i])

        res = ''
        for n in arr:
            if n != 0:
                res += n
            else:
                res += stack.pop()

        return res

    def reverseVowels2(self, s: str) -> str:
        # 双指针
        pool = set('aeiouAEIOU')
        rs = [char for char in s]
        pl = 0
        pr = len(rs)-1
        while pl < pr:
            if rs[pl] in pool and rs[pr] in pool:
                rs[pl], rs[pr] = rs[pr], rs[pl]
                pl += 1
                pr -= 1
            elif rs[pl] not in pool:
                pl += 1
            elif rs[pr] not in pool:
                pr -= 1

        return ''.join(rs)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels2('hello'))
    print(s.reverseVowels2("hello world"))
    print(s.reverseVowels2("leetcode"))

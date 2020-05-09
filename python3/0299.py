class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 52ms:64.13%
        # 13.8mb:12.50%
        # 思路：
        # 公牛：数字猜对，位置也对
        # 奶牛：数字猜对，位置不对
        # 1. 统计猜对的数字个数
        # 2. 统计猜对位置也对的个数
        correct_nums = set(secret).intersection(set(guess))   # 取交集得到都猜对的数字
        pool = {}
        for n in correct_nums:
            pool[n] = min(secret.count(n), guess.count(n))    # 取更小值得到A+B的上限

        A = 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                # 统计数字对位置也对的数量
                A += 1
                pool[secret[i]] -= 1

        # B = 0
        # for k, v in pool.items():
        #     # 剩下的就都是数字对位置不对的
        #     B += v
        B = sum([v for _, v in pool.items()])

        return "{}A{}B".format(A, B)


if __name__ == "__main__":
    s = Solution()
    print(s.getHint("1807", "7810"))
    print(s.getHint("1123", "0111"))

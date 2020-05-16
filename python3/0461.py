class Solution:
    # 汉明距离：两个数字对应**二进制位不同**的位置的数目
    # 所以本质上考虑，就是异或之后含有1的数目
    # 异或：两位相同为0，相异为1
    def hammingDistance(self, x: int, y: int) -> int:
        # 内置函数
        return bin(x ^ y).count("1")

    def hammingDistance2(self, x: int, y: int) -> int:
        # 移位法
        # 对异或之后的数向右移位，逐次判断最后1位是否为1来统计1的个数
        distance = 0
        xor = x ^ y
        while xor:
            if xor & 1:
                # 判断最后1位是否为1，是的话，距离+1
                distance += 1
            xor = xor >> 1

        return distance

    def hammingDistance3(self, x: int, y: int) -> int:
        # 布赖恩·克尼根算法
        # &与运算：相同为1，相异为0
        # 100100 与int(100100,2)-1=100011的&运算结果是100000
        # 能够快速消去最后一个1，操作一次消除1个
        # 因此当结果中不存在1时，得到1的个数
        distance = 0
        xor = x ^ y
        while xor:
            distance += 1
            xor = xor & (xor-1)

        return distance

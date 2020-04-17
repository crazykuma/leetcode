class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 返回阶层中0的数量，主要是返回2*5的数量
        # 因为5出现的次数一定比2少，则只需要考虑出现5的次数即可
        # 而当n是5的倍数的时候，n的阶乘将包含多个5的倍数的值，例如n=25时，20,15,10,5都是5的倍数，因此有n//5=5个值
        # 而25=5*5，因此25包含2个5相乘，因此如果n=25，count=5+1=6，这个1=25//5//5
        # 同理，n=50时，n//5=10,25,50都是多个5相乘的倍数，因此10+2
        # 继续, n=125时，n//5=25,按25有125//25=5,按125有125//125=1，则共有31个
        # 依次类推，有如下解
        count=0
        while n>=5:
            count+=n//5
            n=n//5

        return count

    def trailingZeroes2(self,n:int)->int:
        # 递归解
        # 其实从上文可以分解得到n的阶乘所含0的数量=n//5的个数+（n//5）//5的个数
        # 因此，递归可得
        if n<5:
            return 0
        return n//5+self.trailingZeroes2(n//5)


if __name__ == "__main__":
    s=Solution()
    print(s.trailingZeroes(25)) # 6
    print(s.trailingZeroes(125)) # 31
    print(s.trailingZeroes2(25)) # 6
    print(s.trailingZeroes2(125)) # 31
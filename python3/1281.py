# 注意reduce函数在3.6之后的版本已经被内置移除
from functools import reduce  # 需要增加
class Solution:
    # 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
    def subtractProductAndSum(self, n: int) -> int:
        # 数字转字符串数组
        s = str(n)
        n_list = [int(c) for c in s]
        prod = reduce(lambda a, b: a*b, n_list)
        cumsum = sum(n_list)
        return prod-cumsum

    def subtractProductAndSum2(self, n:int) -> int:
        # 传统数学方法
        prod=1
        cumsum=0
        while n!=0:
            mod=n%10
            prod*=mod
            cumsum+=mod
            n=n//10
        
        return prod-cumsum

if __name__ == "__main__":
    s=Solution()
    assert s.subtractProductAndSum(234)==15
    assert s.subtractProductAndSum2(234)==15
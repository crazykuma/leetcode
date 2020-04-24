from typing import List
""" 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。

 

示例 1：

输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
 """

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # 生成对称数组
        if n % 2 == 0:
            return [i for i in range(1, n+1, 2)]+[i for i in range(-n+1, 0, 2)]
        else:
            return [i for i in range(2, n+1, 2)]+[0]+[i for i in range(-n+1, 0, 2)]

    def sumZero2(self, n: int) -> List[int]:
        # 这个方法更好理解，不用调奇数偶数，步长也可以随意设定
        step=2
        count=1
        res=[]
        k=n
        while n>1:
            res.append(step*count)
            res.append(-step*count)
            count+=1
            n-=2
        
        # n==0orn==1
        if len(res)==k-1:
            res.append(0)

        return res


if __name__ == "__main__":
    s=Solution()
    assert sum(s.sumZero(5))==0
    assert sum(s.sumZero2(5))==0

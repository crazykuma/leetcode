from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 获取最大利润，即所有价格上涨的利润都获取
        # 那么只要计算所有价格上涨空间的和即可
        Profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:      # 价格上涨
                tmp=prices[i]-prices[i-1]  # 计算价格上涨空间
                Profit+=tmp                # 求和
        return Profit    

if __name__ == "__main__":
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([5,4,3,2,1]))
    print(s.maxProfit([]))
    print(s.maxProfit([2,1,2,0,1]))
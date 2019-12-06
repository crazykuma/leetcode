from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只能一次买卖求最大利润
        # 则取之前最小价格与当日价格比较，得到当日利润
        # 逐日比较当日利润，留下最大的。复杂度O(N)
        Profit=0
        s=999999999
        for i in range(1,len(prices)):
            s=min(prices[i-1],s)
            if prices[i]-s>0:
                Profit=max(Profit,prices[i]-s)

        return Profit

if __name__ == "__main__":
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([]))
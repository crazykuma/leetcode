class Solution:
    
    def guessNumber(self, n: int) -> int:
        def guess(n):
            target=2
            if n>target:
                return -1
            if n< target:
                return 1
            if n==target:
                return 0
        l=1
        r=n
        while l<r:
            mid=l+(r-l)//2
            d=guess(mid)
            if d==-1:
                # 在左侧，则缩小右边界
                r=mid-1
            elif d==1:
                # 在右侧，则缩小左边界
                l=mid+1
            elif d==0:
                return mid

        return l

if __name__ == "__main__":
    s=Solution()
    print(s.guessNumber(2))
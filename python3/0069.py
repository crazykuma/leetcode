class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法
        # 执行用时 :60 ms, 在所有 Python3 提交中击败了30.76%的用户
        start=0
        end=x
        while(end>=start):
            m = (end+start)//2
            if m**2<=x and (m+1)**2>x:
                return m
            elif m**2 <= x:
                start=m+1
            elif m**2 > x:
                end = m-1
        
        return m

    def mySqrt3(self, x: int) -> int:
        # 二分查找框架
        left=0
        right=x
        thread=0.0000000001
        while left<right:
            mid=(left+right)/2
            if 0<mid*mid-x<thread:
                return int(mid)
            elif mid*mid>x:
                right=mid-thread
            else:
                left=mid+thread

        return int(left)

    def mySqrt2(self,x:int) -> int:
        # 执行用时 :36 ms, 在所有 Python3 提交中击败了90.52%的用户
        # 牛顿法
        y=x
        while y**2 >x:
            y=(y+x/y)//2
        return int(y)
            

if __name__ == "__main__":
    s=Solution()
    print(s.mySqrt(1))   # 1
    print(s.mySqrt(2))   # 1
    print(s.mySqrt(0))   # 0
    print(s.mySqrt(4))   # 2
    print(s.mySqrt(8))   # 2
    print(s.mySqrt(9))   # 3
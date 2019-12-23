class Solution:
    def isHappy(self, n: int) -> bool:
        i=0
        while i<100:
            n=self.calsquaresum(n)
            i+=1
            if n==1:
                return True
        else:
            return False


    def calsquaresum(self,n:int)-> int:
        s=0
        while n>0:
            m=n%10
            n=n//10
            s=s+pow(m,2)
        
        return s

if __name__ == "__main__":
    s=Solution()
    print(s.isHappy(19))
    print(s.isHappy(8))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1=len(num1)
        n2=len(num2)
        i=0
        j=0
        num1=num1[::-1]
        num2=num2[::-1]
        res=''
        carry=0
        while i<n1 or j<n2:
            tmp=carry
            if i<n1 and j<n2:
                tmp+=int(num1[i])+int(num2[i])
            if i>=n1:
                tmp+=int(num2[j])
            if i>=n2:
                tmp+=int(num1[i])
            if tmp>9:
                carry=1
                res+=str(tmp-10)
            else:
                carry=0
                res+=str(tmp)
            i+=1
            j+=1
        else:
            if carry:
                res+=str(carry)

        return res[::-1]

if __name__ == "__main__":
    s=Solution()
    print(s.addStrings("1","9"))
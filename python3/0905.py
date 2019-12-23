from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd=[] 
        even=[]
        for i in A:
            if i%2:
                odd.append(i)
            else:
                even.append(i)

        return even+odd

if __name__ == "__main__":
    s=Solution()
    print(s.sortArrayByParity([3,1,2,4]))
        
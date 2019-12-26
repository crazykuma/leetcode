from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s=int(''.join([str(e) for e in A]))+K
        return [int(e) for e in str(s)]

if __name__ == "__main__":
    s=Solution()
    print(s.addToArrayForm([1,2,0,0],34)) 
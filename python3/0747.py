from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxN=max(nums)
        idx=nums.index(maxN)
        nums.pop(idx)
        if len(nums)==0:
            return 0
        else:
            for i,n in enumerate(nums):
                if i!=len(nums)-1:
                    if maxN>=2*n:
                        continue
                    else:
                        break                    
                else:
                    if maxN>=2*n:
                        return idx
            return -1

if __name__ == "__main__":
    s=Solution()
    #print(s.dominantIndex([3,6,1,0]))
    #print(s.dominantIndex([1,2,3,4]))
    #print(s.dominantIndex([1]))
    #print(s.dominantIndex([0,0,1,2]))
    print(s.dominantIndex([0,2,0,3]))
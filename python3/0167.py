from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ascending sort numbers
        small=0
        big=len(numbers)-1
        while small<big:
            if numbers[small]+numbers[big]>target:
                big-=1
            elif numbers[small]+numbers[big]<target:
                small+=1
            else:
                return [small+1,big+1]

if __name__ == "__main__":
    s=Solution()
    print(s.twoSum(numbers=[0,1,2,3,7],target=8))
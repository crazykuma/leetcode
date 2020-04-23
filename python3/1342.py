class Solution:
    def numberOfSteps (self, num: int) -> int:
        # 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
        count=0
        while num!=0:
            if num%2==0:
                num=num>>1
            else:
                num-=1
            count+=1
        return count


if __name__ == "__main__":
    s=Solution()
    assert s.numberOfSteps(14)==6
    assert s.numberOfSteps(8)==4
    assert s.numberOfSteps(123)==12
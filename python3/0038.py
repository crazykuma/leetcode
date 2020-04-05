"""
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11                        count:1, num:1
 3.     21                        count:2, num:1
 4.     1211                      count:1,num:2;count:1,num:1
 5.     111221                    count:1,num:1;count:1,num:2;count:2,num:1
 6.     312211                    count:3,num:1;count:2,num:2;count:1,num:1
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # 递归法
        if n == 1:
            return "1"

        l = self.countAndSay(n-1)
        c = l[0]
        count_nums = [1]
        nums = [c]
        idx = 0
        for c in l[1:]:
            if c != nums[-1]:
                idx += 1
                nums.append(c)
                count_nums.append(1)
            else:
                count_nums[idx] += 1

        result = ''.join(str(count_nums[i])+nums[i] for i in range(len(nums)))

        return result


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 11):
        print(s.countAndSay(i))

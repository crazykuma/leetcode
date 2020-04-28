from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        # 双指针
        array = [i for i in range(len(S)+1)]
        i = 0
        j = len(S)
        res = []
        for c in S:
            if c == 'I':
                # 从array中取最小值
                res.append(array[i])
                i += 1
            else:
                res.append(array[j])
                j -= 1
        res.append(array[i])
        return res

    def diStringMatch2(self, S: str) -> List[int]:
        # 用队列和栈的思想
        array = [i for i in range(len(S)+1)]
        res = []
        for c in S:
            if c == 'I':
                # 从array中取最小值
                res.append(array.pop(0))
            else:
                res.append(array.pop())
        res.append(array.pop())
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.diStringMatch("IDID") == [0, 4, 1, 3, 2]
    assert s.diStringMatch("III") == [0, 1, 2, 3]
    assert s.diStringMatch2("DDI") == [3, 2, 0, 1]

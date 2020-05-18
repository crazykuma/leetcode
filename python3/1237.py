"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

from typing import List
# 原题不好理解，所以在这里给出完整的自定义类函数（当然是我加的）


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def __init__(self):
        self.__function_id = 0

    @property
    def id(self):
        return self.__function_id

    @id.setter
    def id(self, function_id):
        self.__function_id = function_id

    def f(self, x, y):
        if self.__function_id == 1:
            return x+y
        if self.__function_id == 2:
            return x*y


class Solution:
    # def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    # 原题不好理解，改成下面这个函数就容易理解了

    def findSolution(self, customfunction: 'CustomFunction', function_id: int, z: int) -> List[List[int]]:
        customfunction.id = function_id   # 提交时注释
        func = customfunction.f
        res = []
        for i in range(1, z+1):
            for j in range(1, z+1):
                if func(i, j) > z:
                    break
                elif func(i, j) == z:
                    res.append([i, j])
        return res


if __name__ == "__main__":
    s = Solution()
    c = CustomFunction()
    print(s.findSolution(customfunction=c, function_id=1, z=5))
    print(s.findSolution(customfunction=c, function_id=2, z=5))

""" 输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
从 [1,1] 到 [3,4] 需要 3 秒 
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒
 """

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        pstart=points.pop(0)
        steps=0
        while points:
            target=points.pop(0)
            x_dif=abs(target[0]-pstart[0])
            y_dif=abs(target[1]-pstart[1])
            # 步数,因为朝任何方向都能走出1步
            # （1，1）和（-1，1）及（0，1），（1，0）在意义上都是等价的，那么肯定存在
            # 当（x_dif,y_dif）存在时，走过min(x_dif,y_dif)+abs(x_dif-y_dif)=max(x_dif,y_dif)即走过距离更长的那段
            steps+=max(x_dif,y_dif)
            pstart=target

        return steps


if __name__ == "__main__":
    s=Solution()
    assert s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])==7

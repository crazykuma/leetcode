from typing import List


case1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
case2 = [["B", "C"], ["D", "B"], ["C", "A"]]
case3 = [["A", "Z"]]


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 差集法：终点集合-起点集合就是剩下的终点
        src = set([x[0] for x in paths])
        des = set([x[1] for x in paths])
        return des.difference(src).pop()

    def destCity2(self, paths: List[List[str]]) -> str:
        # 套娃
        d = {}
        for src, des in paths:
            d[src] = des

        src = paths[0][0]
        while d.get(src):
            src = d[src]

        return src


if __name__ == "__main__":
    s = Solution()
    assert s.destCity(case1) == "Sao Paulo"
    assert s.destCity(case2) == "A"
    assert s.destCity(case3) == "Z"
    assert s.destCity2(case1) == "Sao Paulo"
    assert s.destCity2(case2) == "A"
    assert s.destCity2(case3) == "Z"

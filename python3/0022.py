from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 深度优先搜索
        # 可以将该问题画成一颗二叉树
        # 左支添加左括号，右支添加右括号，则因为括号要成对
        # 所以当剩余的左括号比右括号少时，才可以添加右支
        # 当剩余的左括号和右括号都为0时，找到满足条件的子节点，加入结果集
        res = []

        def dfs(res, left, right, curStr):
            if left == 0 and right == 0:
                res.append(curStr)
                return

            if left > 0:
                # 增加左括号
                dfs(res, left-1, right, curStr+"(")
            if left < right:
                # 括号要成对，先增加了左括号，后增加右括号
                dfs(res, left, right-1, curStr+")")
        dfs(res, n, n, "")
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))

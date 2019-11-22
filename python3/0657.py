class Solution:
    def judgeCircle(self, moves: str) -> bool:
        H=moves.count("U")-moves.count("D")
        L=moves.count("R")-moves.count("L")
        if not H and not L:
            return True
        else:
            return False

if __name__ == "__main__":
    s=Solution()
    print(s.judgeCircle("UD"))
    print(s.judgeCircle("RRDD"))
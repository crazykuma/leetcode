class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count("1")


if __name__ == "__main__":
    s = Solution()
    assert s.hammingWeight(
        int("00000000000000000000000000001011", base=2)) == 3
    assert s.hammingWeight(
        int("00000000000000000000000010000000", base=2)) == 1
    assert s.hammingWeight(
        int("11111111111111111111111111111101", base=2)) == 31

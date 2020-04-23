class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for stone in S:
            if stone in J:
                count+=1
        return count

    def numJewelsInStones2(self, J: str, S: str) ->int:
        # 哈希集合
        Jset=set(J)
        return sum([s in Jset for s in S])


if __name__ == "__main__":
    s=Solution()
    assert s.numJewelsInStones("aA","aAAbbb")==3
    assert s.numJewelsInStones2("aA","aAAbbb")==3
    
class Solution:
    def checkRecord(self, s: str) -> bool:
        l = len(s)
        d = {}
        for i in range(l):
            if s[i] == 'A':
                d[s[i]] = d.get(s[i], 0)+1
                if d[s[i]] > 1:
                    return False
            if s[i] == 'L':
                if i == l-1:
                    return True
                elif i == l-2:
                    return True
                elif i < l-2:
                    if s[i+1] == 'L' and s[i+2] == 'L':
                        return False

        return True

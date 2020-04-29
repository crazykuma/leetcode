from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        while cpdomains:
            click, domain = cpdomains.pop().split(' ')
            while domain:
                d[domain] = d.get(domain, 0)+int(click)
                domain = '.'.join(domain.split('.')[1:])

        return [' '.join([str(v), k]) for k, v in d.items()]


if __name__ == "__main__":
    s = Solution()
    print(s.subdomainVisits(["900 google.mail.com",
                             "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

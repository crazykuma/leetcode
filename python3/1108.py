""" 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
示例 1：

输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
示例 2：

输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"

"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # replace方法
        return address.replace(".","[.]")

    def defangIPaddr2(self, address:str) -> str:
        res=''
        for c in address:
            if c!='.':
                res+=c
            else:
                res+="[.]"
        
        return res

if __name__ == "__main__":
    s=Solution()
    assert s.defangIPaddr("1.1.1.1")=="1[.]1[.]1[.]1"
    assert s.defangIPaddr2("1.1.1.1")=="1[.]1[.]1[.]1"

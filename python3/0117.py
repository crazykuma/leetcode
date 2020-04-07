"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 先层序遍历得到每层的顺序
        # 再对每层进行前后链接，最后一位链接到none
        # 返回链接的结果
        if not root:
            return None
        node=[root]
        
        while node:
            n=len(node)
            queue=[]
            for i in range(n):
                # 先生成下一层的序列
                if node[i].left:
                    queue.append(node[i].left)
                if node[i].right:
                    queue.append(node[i].right)
                if i!=n-1:
                    # 不是最后一个，逐个向右指定
                    node[i].next=node[i+1]
                elif i==n-1:
                    # 最后一个
                    node[i].next=None
            node=queue
            
        return root
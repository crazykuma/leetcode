# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法
        # 要反转单向链表，就需要知道上一项的值，并将当前项指向上一项
        # 因此记录两个指针指向上一项和当前项，将当前指向关系反转后共同前进1位，走到底时，prev=end,cur=none
        prev=None
        cur=head
        while cur:
            temp=cur.next   # 临时存储
            cur.next=prev   # 箭头反向
            prev=cur        # prev前进1位
            cur=temp        # cur 前进1位
        
        return prev
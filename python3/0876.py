# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
        # 如果有两个中间结点，则返回第二个中间结点。
        # 双指针法
        # 快指针依次走两步，慢指针依次走一步
        # 当快指针走到结尾时，慢指针正好走到中间
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        return slow
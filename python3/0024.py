# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 两两一组交换链表中的节点
        # 排除只有1个节点或者没有节点的情况
        # 之前一直纠结传入的是下一个节点体现不出两两一组的情况
        # 原来是一直想错了
        if not head or not head.next:
            return head
        # 选出需要交换的节点
        p1 = head
        p2 = head.next

        p1.next = self.swapPairs(head.next.next)         # 1---> swap(3,4.....)
        p2.next = p1                                     # 2--->1

        return p2

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
        prev = None
        cur = head
        while cur:
            temp = cur.next   # 临时存储
            cur.next = prev   # 箭头反向
            prev = cur        # prev前进1位
            cur = temp        # cur 前进1位

        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        # 递归法
        if not head or not head.next:
            # 当链表为空或者链表只有1位时
            return head

        node = self.reverseList2(head.next)
        # node是返回的根节点
        # 1->2 --->> 1<-2
        head.next.next = head   # head.next代表本来的下一位
        head.next = None

        return node
        # 1->2->3->4->5->NONE
        # 返回node依次是
        # 5->None:head=5
        # 5->4->None:head=4
        # 5->4->3->None:head=3
        # 5->4->3->2->None:head=2
        # 5->4->3->2->1->None:head=1

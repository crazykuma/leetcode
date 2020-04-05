# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 在原来的链表上操作,双指针
        p1=head
        if not head:
            return head
        p2=head.next
        while p2:
            if p2.val == p1.val:
                # 如果遇到重复的，则头指针的下一位为尾指针的下一位，然后移动尾指针
                p1.next=p2.next
                p2=p2.next
            else:
                # 如果不重复，则移动头尾指针至下一位
                p1=p1.next
                p2=p2.next

        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA != pB:
            # 如果两链表有交点，则一定会走相同距离后在某点相遇
            # 如果两链表没有交点，则都会走到对面的null值处判定相等
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        else:
            return pA

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针法
        # 设置快慢两个指针，快指针比慢指针快n步，那么当快指针指向末尾none的时候，慢指针正好指向要删除的节点
        pfast = head
        steps = n
        while steps > 0:
            pfast = pfast.next
            steps -= 1

        pslow = head
        psprev = ListNode(None)
        while pfast:
            pfast = pfast.next
            psprev = pslow
            pslow = pslow.next
        else:
            # pfast==none
            if pslow == head:
                # 删除头节点
                head = head.next
            else:
                # 删除中间节点
                psprev.next = pslow.next

        return head

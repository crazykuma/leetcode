# Definition for singly-linked list.
# 60 ms, 在所有 Python3 提交中击败了97.75%的用户


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 跟字符串加数字一样
        carry = 0
        new = ListNode(0)
        pN = new
        tmp = 0
        while l1 or l2:
            tmp = carry
            # l1 and l2
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tmp += (x+y)
            if tmp > 9:
                carry = 1
                tmp = tmp-10
            else:
                carry = 0

            pN.next = ListNode(tmp)
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            pN = pN.next
        else:
            if carry:
                pN.next = ListNode(1)

        return new.next

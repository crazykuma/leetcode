# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 回文链表
        # 数组双指针法
        if not head:
            return True
        res = []
        while head:
            res.append(head.val)
            head = head.next

        # 对数组进行双指针比较
        i = 0
        j = len(res)-1
        while i <= j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        else:
            return True
    
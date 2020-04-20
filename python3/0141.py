# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 哈希表记录经过的节点，有重复的节点即为环形链表
        d = {}
        start = head
        while start:
            if start in d:
                return True
            else:
                d[start] = 1
            start = start.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        # 双指针法
        # 快指针与慢指针一定会在环形跑道上相遇
        # 排除没有节点和一个节点的情况
        if not head or head.next==None:
            return False
        
        fast=head
        slow=head
        while fast:
            # 快指针如果指向None，那么即非环形
            slow=slow.next if slow else None
            fast=fast.next.next if fast.next else None
            
            if slow == fast:
                # 两个指针相遇时
                return True
        else:
            return False

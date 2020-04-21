# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 旋转链表
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 暴力法：逐步旋转法
        def onestep(head):
            # 逐步旋转
            if not head:
                return None
            if not head.next:
                return head

            # 找到最后一个节点node
            # 将前一个节点的next指向None
            # 将最后一个节点的next指向head
            # 返回最后一个节点node
            pN = head
            while head.next:
                prev = head
                head = head.next
            else:
                # head.next=none
                node = head
                prev.next = None
                node.next = pN

            return node

        if not head:
            return None
        if k == 0:
            return head
        # 找出链表长度
        count = 0
        pC = head
        while pC:
            count += 1
            pC = pC.next
        k = k % count

        for _ in range(k):
            head = onestep(head)

        return head

    def rotateRight2(self, head: ListNode, k: int) -> ListNode:
        # 双指针法
        if not head or k == 0:
            return head
        # 找出链表长度
        count = 0
        pC = head
        while pC:
            count += 1
            pC = pC.next
        k = k % count
        # 排除整除的
        if k == 0:
            return head
        # 快指针先走K步
        steps = k
        fast = head
        while steps > 0:
            fast = fast.next
            steps -= 1

        # 此时慢指针入场，当快指针走到末尾时，慢指针所指即是头节点
        # 快指针的前节点需要指向头节点，而慢指针的前节点需要指向None
        slow = head
        while fast:
            prevf = fast
            fast = fast.next
            prevs = slow
            slow = slow.next

        else:
            #
            prevf.next = head
            prevs.next = None

        return slow

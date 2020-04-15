# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        node = TreeNode(0)
        node.next = head

        preNode, curNode = node, node.next
        while curNode:
            if curNode.val == val:
                # delete
                preNode.next = curNode.next
            else:
                preNode = curNode
            curNode = curNode.next

        return node.next

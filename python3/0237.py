# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 删除链表中的节点
        # 删除链表中某个节点，只需要改变该节点的两个属性，1是值需要前进一格，2是链表的下一项要前进一格
        node.val = node.next.val
        node.next = node.next.next

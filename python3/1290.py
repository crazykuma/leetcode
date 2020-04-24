# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary=[]
        while head:
            binary.append(head.val)
            head=head.next
            
        l=len(binary)-1
        b=0
        for i in range(l,-1,-1):
            b+=binary[i]*pow(2,l-i)

        return b
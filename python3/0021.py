# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None: return l2   # 判断l1不为空，否则输出l2
        if l2==None: return l1   # 判断l2不为空，否则输出l1
        new=ListNode(None)       # 新建一个空节点
        pN = new                 # 新建一个指针指向空节点
        while l1 and l2:        
            if l1.val < l2.val:   
                pN.next = l1     # 将空节点的指针指向l1
                l1 = l1.next     # l1指向l1后面的节点
            else:
                pN.next=l2       # l2值小，则指向l2
                l2 = l2.next     # l2指向l2后面的节点
            pN = pN.next         # 移动新节点的指针到下一位，等待指向l1或者l2
        
        pN.next=l1 if l1 else l2 # 当l1和l2长度不等时，l1或者l2后续部分接上新节点
        return new.next          # 返回从空节点起的节点

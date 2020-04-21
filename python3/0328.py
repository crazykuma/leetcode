# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 双指针法，参考官方题解
        # 本来想了一个快慢指针的走法，但是快指针每步步长需要变化，没有题解的这个方法简单
        # 奇数指针走奇数位，偶数指针走偶数位
        # 返回奇数链表+偶数链表
        if not head:
            # 不存在链表的情况
            return head
        odd=head                       # 奇数位
        even=head.next                 # 偶数位
        evenhead=even                  # 标定初始偶数位作为偶数链表的头
        while even and even.next:      # 排除只有两个节点的情况
            odd.next=even.next         # 奇数链直接指向偶数的下一位
            odd=odd.next               # 将奇数指针前移到下一个奇数位上
            
            even.next=odd.next         # 变更偶数节点的指向为下一个偶数位
            even=even.next             # 将偶数位节点前移
                                       # 因为evenhead指向初始偶数位，而偶数链关系一直延续
        odd.next=evenhead              # 因此在末尾处当末尾是偶数节点时，奇数链舍弃最后一位接上偶数链，是要求的链表
                                       # 而末尾是奇数节点时，奇数链接上偶数链正好是要求的链表
        return head

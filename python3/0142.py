# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 哈希表解法
        # 走一圈在哈希表中记录下位置，当出现第一个重复位置的时候返回其坐标
        d = {}
        while head:
            if head not in d:
                d[head] = 1
                head = head.next
            else:
                return head
        else:
            return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        # 双指针解法
        # 设置快慢指针，当第一次相遇时，慢指针走过n步，快指针走过2n步
        # 假设起点到环形入口的距离是a，那么n=a+b,b是环内走过的步数
        # 同样可以知道2n=a+b+c,c是环的长度
        # a=n-b,n=c,a=c-b,c-b就是慢指针走到环形起点剩下的距离，而a则是从起点到环形起点的距离
        # 因此慢指针走c-b步，和从起点走a步是一样的，所以再加入一个从起点的指针走a步就能够找到环形起点的位置
        if not head or not head.next:
            return None
        
        fast=head
        slow=head
        while fast:
            fast=fast.next.next if fast.next else None
            slow=slow.next if slow else None
            if fast==slow:
                break
        else:
            return None
        
        find=head
        while find!=slow:
            find=find.next
            slow=slow.next

        return find

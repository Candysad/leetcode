#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        O(1) 空间
        3个指针，head留下不动，快慢两个进去追
        快的变成None则无环
        追上了则有坏，快的定住不动，慢的在环中循环
        慢的如果是head 或 head的next，则找到进环的位置
        转了一圈没找的则head往后挪一个，慢的再来一圈
        '''
        
        '''
        fast = 2 * low
        fast = low + n * circle
        low = n * circle
        追上的时候慢的走的距离刚好是n圈，再走target长度就回到起点
        
        low + target = target + n * circle
        '''
        if head is None or head.next is None:
            return None
        
        low, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            low = low.next
            
            if low == fast:
                break
            
        if fast is None or fast.next is None:
            return None
        
        fast = head
        while fast != low:
            fast= fast.next
            low = low.next
        
        return low
        
        '''
        普通办法，类似两数之和
        '''
        pre = set()
        while head is not None:
            if head.next in pre:
                return head.next
            
            pre.add(head)
            head = head.next
        return None
# @lc code=end


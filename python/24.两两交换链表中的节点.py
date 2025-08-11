#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        left, right, last = head, head.next, ListNode(next=head)
        head = last
        while left and right:
            last.next = right
            left.next = right.next
            right.next = left
            
            last = left
            left = left.next
            right = left.next if left else None
        
        return head.next
# @lc code=end


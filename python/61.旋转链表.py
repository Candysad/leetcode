#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # 找总长度
        n, right = 1, head
        while right.next:
            n += 1
            right = right.next
        k %= n
        right.next = head # 接头
        
        # 找新的开头
        t, left = 0, head
        while t < n - k - 1: # 停在新开头的上一个，把它们断开
            left = left.next
            t += 1
        result = left.next
        left.next = None
        
        return result   
# @lc code=end
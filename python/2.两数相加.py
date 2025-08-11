#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        now = result
        carry = 0
        
        while now:
            now.val = carry
            if l1:
                now.val += l1.val
                l1 = l1.next
            if l2:
                now.val += l2.val
                l2 = l2.next

            carry = int(now.val/10) #进位
            now.val %= 10 # 当前位
            
            if carry or l1 or l2: # 没算完就继续
                now.next = ListNode()

            now = now.next
        return result
# @lc code=end


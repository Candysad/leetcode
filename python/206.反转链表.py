#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        t = ListNode()
        t.next = head
        
        # 左右两个指针，让右边的节点指向左边
        # 用 t 记录本来右边的下一个用于进入下一步
        left, right = t, head
        while right != None:
            t = right.next
            right.next = left
            
            left, right = right, t
        
        # 拿走虚空起点
        # head.next = None
        return left
        
# @lc code=end


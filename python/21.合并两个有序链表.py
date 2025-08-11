#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            head = list1 
            now = list1
            list1 = list1.next
        else:
            head = list2
            now = list2
            list2 = list2.next
        
        while list1 and list2:
            if list1.val <= list2.val:
                now.next = list1
                list1 = list1.next
            else:
                now.next = list2
                list2 = list2.next
            now = now.next
        
        now.next = list1 if list1 else list2
        
        return head
                
        
# @lc code=end


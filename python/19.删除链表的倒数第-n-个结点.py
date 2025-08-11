#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        数据结构在本质上决定了都得扫2遍
        取巧方法只是写了一次循环，本质上还是用了两个变量相当于两次遍历
        '''
        '''
        双指针
        '''
        right = head
        count = 0
        while right != None:
            count += 1
            right = right.next
        
        if n == count:
            return head.next
        
        left = head
        for i in range(count - n - 1):
            left = left.next
        
        left.next = left.next.next
        return head   
# @lc code=end


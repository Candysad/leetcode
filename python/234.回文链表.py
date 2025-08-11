#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        时间换空间
        栈
        '''
        # 第一遍找长度
        total = 0
        node = head
        while node is not None:
            total += 1
            node = node.next
        
        if total == 1:
            return True
        
        # 前一半进栈
        half = total // 2 # 只要前一半的个数
        node = head
        count = 0
        stack = []
        while count < half:
            stack.append(node.val)
            node = node.next
            count += 1
        
        if total % 2: # 跳过奇数中间那个
            node = node.next
        
        # 后一半和前一半比较
        while node is not None:
            if stack.pop() != node.val:
                return False
            node = node.next
        
        return True
    
        '''
        空间换时间则遍历一遍全存下来然后前后俩指针比较
        '''
# @lc code=end


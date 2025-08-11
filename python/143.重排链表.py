#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        right = head
        length = 0
        while right.next:
            right = right.next
            length += 1
        
        if length < 2:
            return head
        if length == 2:
            right.next = head.next
            right.next.next = None
            head.next = right
            return head
        
        # 超过四个再考虑翻转后半部
        # 因为超过四个后半部才有超过2个节点，才可以开始翻
        
        rstart = length // 2
        right = head
        for i in range(rstart):
            right = right.next
        # right现在是左半部分的最后一个
       
        rightright = right.next
        t = rightright.next
        # 右半部新结尾置空
        rightright.next = None
        # 左半部新结尾置空
        right.next = None
        
        # 有下一个才往前循环
        while t:
            right, rightright, t = rightright, t, t.next
            rightright.next = right
        
        right = rightright
        left = head
        
        # 穿起来
        now = ListNode()
        while left:
            now.next = left
            now = now.next
            left = left.next
            
            now.next = right
            if right:# 总要挪到空为止，不能下一个是空就不挪了
                right = right.next
            now = now.next
        
# @lc code=end


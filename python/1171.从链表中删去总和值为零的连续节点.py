#
# @lc app=leetcode.cn id=1171 lang=python3
#
# [1171] 从链表中删去总和值为零的连续节点
#
from bisect import bisect_left
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        stack = [[0, sentinel]]
        pre = {0: sentinel}
        
        now = head
        i = 1
        while now:
            t = stack[-1][0] + now.val
            if t in pre:
                last = pre[t]
                while stack[-1][1] != last:
                    del pre[stack.pop()[0]]
            
            else:
                stack.append([t, now])
                pre[t] = now
        
            now = now.next
            i += 1
            
        last = sentinel
        for _, node in stack:
            last.next = node
            last = node
        last.next = None
        return sentinel.next
        
# @lc code=end


#
# @lc app=leetcode.cn id=1474 lang=python3
#
# [1474] 删除链表 M 个节点之后的 N 个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        def move(now, t):
            node = now
            for i in range(t):
                if node == None: return None
                node = node.next
            return node
        
        sentinel = ListNode(next=head)
        now = sentinel
        while True:
            now = move(now, m)
            if now is None:
                return sentinel.next
            
            nxt = move(now, n)
            if nxt is None:
                now.next = None
                return sentinel.next
            now.next = nxt.next
            
            now = nxt
# @lc code=end
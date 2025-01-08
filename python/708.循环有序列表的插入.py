#
# @lc app=leetcode.cn id=708 lang=python3
#
# [708] 循环有序列表的插入
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            result = Node(val=insertVal)
            result.next = result
            return result
        
        pre = head
        now = head.next
        while True:    
            if now is head:
                pre.next = Node(val=insertVal, next=head)
                return head
            
            if pre.val <= insertVal <= now.val:
                pre.next = Node(val=insertVal, next=now)
                return head
            
            if pre.val > now.val:
                if insertVal <= now.val or insertVal > pre.val:
                    pre.next = Node(val=insertVal, next=now)
                    return head
            
            pre = now
            now = now.next
# @lc code=end
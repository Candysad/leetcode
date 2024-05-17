#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 虚空头，用于返回
        originhead = Node(x=0, next=head)
        copyhead = Node(0)
        
        origin = head
        copy = copyhead
        # 存2个链表的节点
        # 旧的存 节点：序号
        # 新的存 序号：节点
        originset = {None: None}
        copyset = {None: None}
        i = 0
        # 复制一遍基本值
        while origin:
            originset[origin] = i
            
            copy.next = Node(x = origin.val)
            copy = copy.next
            copyset[i] = copy
            
            i += 1
            origin = origin.next
   
        # 按照序号复制 random
        origin = originhead.next
        copy = copyhead.next
        while origin:
            target = originset[origin.random]
            copy.random = copyset[target]
            origin = origin.next
            copy = copy.next
        
        return copyhead.next

# @lc code=end


#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from heapq import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        优先队列
        '''
        # if head is None:
        #     return None
        
        # nodes = {}
        # queue = []
        # node = head
        # i = 0
        # while node is not None:
        #     nodes[i] = node
        #     heappush(queue, (node.val, i))
        #     node = node.next
        #     i += 1
        
        # result = ListNode()
        # last = result
        # while queue:
        #     _, i = heappop(queue)

        #     last.next = nodes[i]
        #     last = last.next
        #     last.next = None
            
        
        # return result.next
        
        if head is None:
            return None
        node = head
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        
        nums.sort()
        i = 0
        node = head
        while node:
            node.val = nums[i]
            node = node.next
            i += 1
        return head   
# @lc code=end


#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from heapq import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        '''
        优先队列 (val, node)
        '''
        result = ListNode()
        last = result
        
        queue = []
        for i, node in enumerate(lists):
            if node is not None:
                heappush(queue, (node.val, i))
        
        while queue:
            val, i = heappop(queue)
            
            last.next = lists[i]
            last = last.next
            
            if lists[i].next is not None:
                heappush(queue, (lists[i].next.val, i))
            
            lists[i] = lists[i].next
        
        return result.next
        
        '''
        依次循环
        时间复杂度 O(n^2)
        原地重新排，空间复杂度O(n*m) 链个数*链长度
        '''
        # # 还有没有节点
        # def check_for_min():
        #     t = 0
        #     for i in range(len(lists)):
        #         if lists[i] is not None:
        #             if lists[t] is None:
        #                 t = i
        #             elif lists[i].val < lists[t].val:
        #                 t = i
        #     return t
        
        # head = ListNode()
        # now = head
        # min_node = check_for_min()
        # while lists[min_node] is not None:
        #     now.next = lists[min_node]
        #     lists[min_node] = lists[min_node].next
        #     now = now.next
            
        #     min_node = check_for_min()
            
        # return head.next
        
        '''
        全拿出来排序
        时间复杂度 min( O(n*m) , O(logn)) 遍历时间与排序时间
        '''
        # nums = []
        # for link in lists:
        #     while link:
        #         nums.append(link.val)
        #         link = link.next
        
        # nums.sort()
        # head = ListNode()
        # now = head
        # for n in nums:
        #     now.next = ListNode(val=n)
        #     now = now.next
        
        # return head.next
# @lc code=end
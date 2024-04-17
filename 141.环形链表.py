#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        快慢指针
        
        如果无环，则会跑到None
        如果有环，在环里快的会追上慢的
        
        额外空间为O(1) 但是时间不定
        '''
        
        '''
        无要求的话可以修改节点的值或next
        再次遍历到修改后的特殊值则说明有环
        '''
        
        '''
        存前面遍历过的
        '''
        # pre = set()
        # while head is not None:
        #     if head in pre:
        #         return True
        #     pre.add(head)
        #     head = head.next
        
        # return False
        
        '''
        如果有环则最多转1圈 10000还没出来
        '''
        # count = 0
        # while head is not None and count < 10001:
        #     head = head.next
        #     count += 1
        
        # if head is None:
        #     return False
        
        # return True
# @lc code=end


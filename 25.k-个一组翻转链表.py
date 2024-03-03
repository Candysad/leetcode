#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        双指针
        右指针侦察
            满足个数则左指针出发调转
            不满足个数则停止
        '''
        if k == 1:
            return head
        
        def reverse(node, k):
            right = node
            count = 0
            while right: # 侦察
                count += 1
                right = right.next
            if count < k: # 不够了
                return node, None 

            last = node # 开头变成结尾
            count = 0
            left, right = node, node.next
            while count < k-1:
                count += 1
                if count == k-1:
                    head = right
                
                t = right.next
                right.next = left # right 最后一次指向下一组的开始
                left = right
                right = t
            
            last.next = right # 新的结尾接上下一组目前的开始
            return head, last # 返回新的开头和新的结尾

        head, now = reverse(head, k)
        while now:
            last = now # now 是上一组的结尾，用 last 记录
            now = now.next # now 指向下一组的开始
            t_head, now = reverse(now, k)
            last.next = t_head # 上一组结尾接上下一组开始
        return head
# @lc code=end


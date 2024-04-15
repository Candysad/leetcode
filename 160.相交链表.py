#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        也可以看成两条赛道，把两条赛道都跑一遍才算完成比赛
        这样两个人跑的距离都一样，起点不同但是终点相同、
        因为终点相同、速度相同、距离也相同，最后会同时停在同一个位置
        
        如果没有相交的位置，则两条跑道跑完了也不会停在相交的位置，而是同时停在各自的None，即各自第二段赛道的终点
        '''
        a, b = headA, headB
        while a is not b:# 要么相交，要么同时到达 None
                         # 如果两赛道长度相同，会同时第一次到达None，那也会先同时到达交叉点
            a = a.next if a is not None else headB # 自己第一段跑完了就换赛道
            b = b.next if b is not None else headA
        
        return a
        
        
        # a = set()
        # while headA is not None:
        #     a.add(headA)
        #     headA = headA.next
        # while headB is not None:
        #     if headB in a:
        #         return headB
        #     headB = headB.next
        # return None
        
# @lc code=end


#
# @lc app=leetcode.cn id=2462 lang=python3
#
# [2462] 雇佣 K 位工人的总代价
#
from heapq import *
from math import inf
# @lc code=start
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 + k > n:
            costs.sort()
            return sum(costs[:k])
        
        front = costs[:candidates]
        back = costs[-candidates:]
        heapify(front)
        heapify(back)
        left = candidates
        right = n - candidates - 1
        
        result = 0
        while k > 0:
            if front[0] <= back[0]:
                result += heapreplace(front, costs[left])
                left += 1
            else:
                result += heapreplace(back, costs[right])
                right -= 1
            k -= 1
        return result
        
        # n = len(costs)
        # front = [(costs[i], i) for i in range(candidates)]
        # back = [(costs[i], i) for i in range(n-1, n-candidates-1, -1)]
        # heapify(front)
        # heapify(back)
        # left = candidates
        # right = n - candidates - 1
        # vis = set()
        
        # for i in range(k):
        #     # 每轮开始找左右最小的，同时把已经用过的弹出
        #     # 按理说弹出一个就该补一个，但是所有交叉导致的弹出都在选择的时候提前补了一个
        #     # 直接选择的弹出也立即就补了一个
        #     while front and front[0][1] in vis:
        #         heappop(front)
        #     leftmin = front[0] if front else (inf, n)
            
        #     while back and back[0][1] in vis:
        #         heappop(back)
        #     rightmin = back[0] if back else (inf, -1)
            
        #     # 从左边取
        #     if leftmin <= rightmin:
        #         heappop(front)
        #         vis.add(leftmin[1])
                
        #         #  左边补一个
        #         if left < n:
        #             heappush(front, (costs[left], left))
        #             left += 1
                
        #         # 该元素如果在左右交叉的部分里
        #         # 该元素从右边弹出在之后发生，先把新的元素补进去
        #         if right > -1 and leftmin[1] > right:
        #             while right in vis: # 跳过已经用过的部分
        #                 right -= 1
        #             if right > -1:
        #                 heappush(back, (costs[right], right))
        #                 right -= 1
            
        #     # 从右边取
        #     else:
        #         heappop(back)
        #         vis.add(rightmin[1])
                
        #         # 右边补
        #         if right > -1:
        #             heappush(back, (costs[right], right))
        #             right -= 1
                
        #         # 如果该元素也在左边，给左边先补一个
        #         if left < n and rightmin[1] < left:
        #             while left in vis:
        #                 left += 1
        #             if left < n:
        #                 heappush(front, (costs[left], left))
        #                 left += 1
        # result = 0
        # for i in vis:
        #     result += costs[i]
        # return result
# @lc code=end


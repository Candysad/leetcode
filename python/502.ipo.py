#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
from heapq import *
# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        items = list(zip(profits, capital))
        items = sorted(items, key=lambda x: (x[1]))
        n = len(profits)
        
        queue = []
        i = 0
        for _ in range(k):
            while i < n and items[i][1] <= w:
                heappush(queue, -items[i][0])
                i += 1

            if queue:
                w += -heappop(queue)
            else:
                return w
            
        return w
# @lc code=end
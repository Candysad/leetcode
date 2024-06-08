#
# @lc app=leetcode.cn id=2931 lang=python3
#
# [2931] 购买物品的最大开销
#
from heapq import *
# @lc code=start
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0])
        queue = [(values[i][-1], i, n-1) for i in range(m)]
        heapify(queue)
        
        result = 0
        day = 1
        while queue:
            value, i, j = heappop(queue)
            result += day * value
            day += 1
            j -= 1
            if j >= 0:
                heappush(queue, (value[i][j], i, j))
        
        return result
# @lc code=end


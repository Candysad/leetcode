#
# @lc app=leetcode.cn id=1824 lang=python3
#
# [1824] 最少侧跳次数
#
from math import inf
# @lc code=start
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp0 = [inf, 0, inf]
        
        for i in range(1, n):
            if obstacles[i] == 0:
                continue
            
            dp1 = dp0.copy()
            dp1[obstacles[i]-1] = inf
            for j in range(3):
                if dp1[j] == inf and obstacles[i-1]-1 != j and obstacles[i]-1 != j:
                    dp1[j] = min(dp0) + 1
                    
            dp0 = dp1
            
        return min(dp0)
# @lc code=end


#
# @lc app=leetcode.cn id=1937 lang=python3
#
# [1937] 扣分后的最大得分
#
from itertools import accumulate
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0]
        
        for i in range(1, m):
            pre = list(accumulate([d + j for j, d in enumerate(dp)], max))
            suf = list(accumulate([d - j for j, d in enumerate(dp)][::-1], max))[::-1]
            
            for j in range(n):
                dp[j] = max(pre[j] - j, suf[j] + j)  + points[i][j]
                
        return max(dp)
# @lc code=end
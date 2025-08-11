#
# @lc app=leetcode.cn id=1334 lang=python3
#
# [1334] 阈值距离内邻居最少的城市
#
from math import inf
# @lc code=start
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        
        sign = True
        while sign:
            sign = False
            
            for a, b, w in edges:
                for node1 in range(n):
                    if dp[node1][b] > dp[node1][a] + w:
                        sign = True
                        dp[node1][b] = dp[node1][a] + w
                    if dp[node1][a] > dp[node1][b] + w:
                        sign = True
                        dp[node1][a] = dp[node1][b] + w
        
        result = -1
        c = inf
        for i in range(n):
            t = 0
            for j in range(n):
                if j == i: continue
                if dp[i][j] <= distanceThreshold:
                    t += 1
            if t <= c:
                result = i
                c = t
        return result
# @lc code=end


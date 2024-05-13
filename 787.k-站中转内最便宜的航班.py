#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        递归
        '''
        # g = [[] for _ in range(n)]
        # for node1, node2, p in flights:
        #     g[node1].append((node2, p))
        
        # @cache
        # def dfs(i, k):
        #     if i == dst:
        #         if k != -1:
        #             return 0
        #         else:
        #             return inf
        #     if k == 0:
        #         return inf
            
        #     t = inf
        #     for j, w in g[i]:
        #         t = min(t, dfs(j, k-1) + w)
        #     return t

        # result = dfs(src, k+1)
        # return result if result != inf else -1

        '''
        DP
        dp[node][step] 第step步到node，g里反着存然后找来源
        '''
        g = [[] for _ in range(n)]
        for node1, node2, p in flights:
            g[node2].append((node1, p))
        dp = [[inf] * (k+2) for _ in range(n)]
        dp[src][0] = 0
        
        for i in range(1, k+2):
            for node2 in range(n):
                for node1, p in g[node2]:
                    dp[node2][i] = min(dp[node1][i-1] + p, dp[node2][i])
        
        result = min(dp[dst])
        return result if result != inf else -1
# @lc code=end
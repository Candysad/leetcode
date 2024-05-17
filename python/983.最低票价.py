#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#
from math import inf
# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        递归
        看起来像数组维护DP
        但是不论是跳步还是天数都不是离散的
        递归可以清晰直观的描述
        '''
        # last = days[-1]
        # days = set(days)
        
        # @cache
        # def dfs(i):
        #     nonlocal days, costs
            
        #     if i > last:
        #         return 0
            
        #     # 今天不用出行
        #     if i not in days: 
        #         return dfs(i+1)
            
        #     # 今天需要出行
        #     # 1 天票
        #     c1 = costs[0] + dfs(i+1)
            
        #     # 7 天票
        #     c7 = costs[1] + dfs(i+7)
            
        #     # 30 天票
        #     c30 = costs[2] + dfs(i + 30)
            
        #     return min(c1, c7, c30)
        
        
        # return dfs(1)
        
        '''
        从递归改成数组维护DP
        
        dp[i] 表示今天刚好没通行证的状态，要花的最少支出（不算今天的支出）
        dp[i] 
            如果今天不用出行，那就是昨天的状态
            dp[i-1]
            
            如果今天要出行
                1前天买了1天票
                dp[i-1] + cost[0]
                
                7天前买了7天票今天过期
                dp[i-7] + cost[7]
                
                30天前买了30天票今天过期
                dp[i-30] + cost[7]
        '''
        n = days[-1]
        days = set(days)
        dp = [inf] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            if i not in days:
                dp[i] = dp[i-1]
            
            else:
                t1 = dp[i-1] + costs[0]
                t2 = costs[1] if i < 7 else dp[i-7] + costs[1]
                t3 = costs[2] if i < 30 else dp[i-30] + costs[2]
                
                dp[i] = min(t1, t2, t3)
        return dp[-1]
# @lc code=end
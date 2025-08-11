#
# @lc app=leetcode.cn id=2585 lang=python3
#
# [2585] 获得分数的方法数
#

# @lc code=start
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(types)
        dp = [1] + [0] * target
        
        for count, coin in types:
            tdp = [0] * (target + 1)
            for i in range(1, count+1):
                d = i * coin
                if target < d: break
                
                for t in range(target, 0, -1):
                    if t < d: break
                    
                    tdp[t] += dp[t - d]            
            
            for i, t in enumerate(tdp):
                dp[i] += t
                dp[i] %= mod
                
        return dp[-1] % mod
# @lc code=end
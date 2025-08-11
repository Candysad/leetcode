#
# @lc app=leetcode.cn id=1406 lang=python3
#
# [1406] 石子游戏 III
#
from math import inf
# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * n + [0] * 3
        _sum = 0
        for i in range(n-1, -1, -1):
            _sum += stoneValue[i]
            pre = min(dp[i+1], dp[i+2], dp[i+3])
            
            dp[i] = _sum - pre
        
        if dp[0] > _sum - dp[0]:
            return 'Alice'
        elif dp[0] < _sum - dp[0]:
            return 'Bob'
        return 'Tie'
# @lc code=end
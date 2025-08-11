#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
mod = 10**9 + 7
dp = [1, 1, 2, 5] + [0] * 1000
for i in range(4, 1001):
    dp[i] = (2*dp[i-1] + dp[i-3]) % mod
class Solution:
    def numTilings(self, n: int) -> int:
        '''
        https://leetcode.cn/problems/domino-and-tromino-tiling/solutions/1968516/by-endlesscheng-umpp/?envType=study-plan-v2&envId=dynamic-programming
        '''
        return dp[n]
        
# @lc code=end


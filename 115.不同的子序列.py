#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        动态规划
        状态 (i,j) 指s[0..i]可以组成多少种 t[0..j]
        转移 (i,j) 由 (i, j-1) (i-1,j-1)决定
                    s[i] t[j] 相同，则出现 1*dp[i-1][j-1]个新组合
                                     并加上此时 dp[i-1][j] 的组合
                    如果不相同，则只有 dp[i-1][j]
        '''
        mod = 10**9 + 7
        m = len(s)
        n = len(t)
        if n > m:
            return 0
        
        dp = [[0]* (n+1) for _ in range(m+1)]
        for i in range(m+1): # s总包含空串
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, min(i+1, n+1)): # t 长度不超过 s # 倒着维护可以避免这个 min
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i-1] == t[j-1] else dp[i-1][j] #末尾新s没匹配上，那就用s前面的匹配当前t
        
        return dp[-1][-1] % mod
        
        
        
# @lc code=end


#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#

# @lc code=start
class Solution:
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        # 72 编辑距离 替换、增删
        # 712 只删除，两边都删
        
        状态 当前(0..i, 0..j) 位置最小的删除和
        转移 在 (i-1, j-1) (i, j-1) (i-1, j) 中选修改当前（考虑之前状态条件）后最小的
        '''
        
        m = len(s1)
        n = len(s2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 边界条件
        # s1 不空，s2空：
        # 让i-1的s1变为空，再删去当前的i
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] # 如果一样就不用删
                else: # 如果不一样就考虑删哪个
                      # (i-1, j) 上一个s1 和当前 s2完成对齐，多的是s1最新的 i， 所以删去i
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1]+ ord(s2[j-1]))
        
        return dp[-1][-1]

# @lc code=end


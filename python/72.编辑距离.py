#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m+1):
            dp[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]
        

        '''
        动态规划
        前面不管怎么变，就当x次变化使(i-1, j-1) (i-1, j) (i, j-1) 一致
        要使当前一致，若相同就不用变，若不同就修改一次
        
        边界
            一方是空的，则增加另一方长度变成另一方
            另一方是空的，则删除自己这一方变成空的
        '''
        # m = len(word1)
        # n = len(word2)
        # if m*n == 0:
        #     return m+n
        
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # # 目标是空的，依次删除自己
        # for i in range(m+1):
        #     dp[i][0] = i
        # # 当前自己是空的，依次加入目标长度
        # for i in range(n+1):
        #     dp[0][i] = i
        
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if word1[i-1] == word2[j-1]: # 如果当前相等
        #                                      # (i-1, j-1) 则对应双方都增加一个，其实不用变
        #                                      # (i-1, i) (i, j-1) 之前都一样了又出来一个，删掉或加上
        #             dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
        #         else:
        #             dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        # return dp[-1][-1]
        
# @lc code=end


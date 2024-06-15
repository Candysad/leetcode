#
# @lc app=leetcode.cn id=1301 lang=python3
#
# [1301] 最大得分的路径数目
#

# @lc code=start
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7
        n = len(board)
        dp = [[[0, 0] for __ in range(n)] for _ in range(n)]
        dp[-1][-1][1] = 1
            
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                num = board[i][j]
                if '1' <= num <= '9':
                    num = int(num)
                elif num == 'E':
                    num = 0
                else: continue
                
                t, c = 0, 0
                if i < n-1:
                    if dp[i+1][j][0] > t:
                        t, c = dp[i+1][j]
                    elif dp[i+1][j][0] == t:
                        c += dp[i+1][j][1]

                if j < n-1:
                    if dp[i][j+1][0] > t:
                        t, c = dp[i][j+1]
                    elif dp[i][j+1][0] == t:
                        c += dp[i][j+1][1]

                if i < n-1 and j < n-1:
                    if dp[i+1][j+1][0] > t:
                        t, c = dp[i+1][j+1]
                    elif dp[i+1][j+1][0] == t:
                        c += dp[i+1][j+1][1]

                dp[i][j][0], dp[i][j][1] = t + num, c % mod
                    
        return dp[0][0] if dp[0][0][1] > 0 else [0, 0]       
# @lc code=end
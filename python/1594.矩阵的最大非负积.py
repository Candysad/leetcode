#
# @lc app=leetcode.cn id=1594 lang=python3
#
# [1594] 矩阵的最大非负积
#

# @lc code=start
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        g1 = len(grid)
        g2 = len(grid[0])
        # None 表示没有正的或负的
        dp = [[[None, None] for __ in range(g2)] for _ in range(g1)]

        for i in range(g1):
            for j in range(g2):
                num = grid[i][j]
                
                if num == 0: # 当前为 0，则正负乘了都变成 0
                    dp[i][j] = [0, 0]
                elif num > 0: # > 0
                    if i == j == 0: # 第一个数
                        dp[i][j][0] = num
                        continue
                    
                    if i-1 >= 0: # 有上面一行，用它的正负来更新当前位置
                        p, n = dp[i-1][j]
                        if p is not None:
                            dp[i][j][0] = p * num
                        if n is not None:
                            dp[i][j][1] = n * num
                    
                    if j-1 >= 0: # 有左边一列
                        p, n = dp[i][j-1]
                        if p is not None:
                            if dp[i][j][0] is not None:
                                dp[i][j][0] = max(dp[i][j][0], p * num)
                            else:
                                dp[i][j][0] = p * num
                        if n is not None:
                            if dp[i][j][1] is not None:
                                dp[i][j][1] = min(dp[i][j][1], n * num)
                            else:
                                dp[i][j][1] = n * num
                else: # 当前为负
                    if i == j == 0:
                        dp[i][j][1] = num
                        continue
                    
                    if i-1 >= 0:
                        p, n = dp[i-1][j]
                        if n is not None:
                            dp[i][j][0] = n * num
                        if p is not None:
                            dp[i][j][1] = p * num
                    
                    if j-1 >= 0:
                        p, n = dp[i][j-1]
                        if n is not None:
                            if dp[i][j][0] is not None:
                                dp[i][j][0] = max(dp[i][j][0], n * num)
                            else:
                                dp[i][j][0] = n * num
                        if p is not None:
                            if dp[i][j][1] is not None:
                                dp[i][j][1] = min(dp[i][j][1], p * num)
                            else:
                                dp[i][j][1] = p * num
        # 返回最后一个正数
        result = dp[-1][-1][0]
        return result % mod if result is not None else -1
# @lc code=end
#
# @lc app=leetcode.cn id=1301 lang=python3
#
# [1301] 最大得分的路径数目
#
from functools import cache
# @lc code=start
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7
        n = len(board)
        
        @cache
        def dfs(i, j):
            if i == n-1 and j == n-1: return 0, 1
            if i == n or j == n: return -1, 0
            if board[i][j] == 'X': return -1, 0
            
            num = int(board[i][j]) if board[i][j] != 'E' else 0
            t1, c1 = dfs(i+1, j)
            t2, c2 = dfs(i, j+1)
            t3, c3 = dfs(i+1, j+1)
            
            if t1 == t2:
                c1 += c2
            elif t1 < t2:
                t1 = t2
                c1 = c2
            
            if t1 == t3:
                c1 += c3
            elif t1 < t3:
                t1 = t3
                c1 = c3
            
            return t1 + num, c1 % mod
        
        result = dfs(0, 0)
        return result if result[1] != 0 else [0, 0]
# @lc code=end
#
# @lc app=leetcode.cn id=2328 lang=python3
#
# [2328] 网格图中递增路径的数目
#
from functools import cache
# @lc code=start
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        
        @cache
        def dfs(i, j):
            num = grid[i][j]
            t = 1
            for x, y in [(i, j + 1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] > num:
                        t += dfs(x, y)
            
            return t % mod
        
        result = 0
        for i in range(m):
            for j in range(n):
                result += dfs(i, j)
                result %= mod
        return result
        
# @lc code=end
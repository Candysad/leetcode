#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def flipcolumn(i):
            for j in range(n):
                grid[i][j] = 1- grid[i][j]
        def fliprow(j):
            for i in range(m):
                grid[i][j] = 1- grid[i][j]
        def check(j):
            result = 0
            for i in range(m):
                if grid[i][j] == 1: result += 1
            return result < m - result
        
        for i in range(m):
            if grid[i][0] == 0:
                flipcolumn(i)
        
        for j in range(n):
            if check(j):
                fliprow(j)
        result = 0
        for i in range(m):
            for j in range(n):
                result += grid[i][j] * 2**(n-1-j)
        return result
# @lc code=end
#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
from functools import cache
# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        starts = []
        def startcheck(i, j):
            for x, y in [
                            (i-1, j),
                (i,   j-1)          , (i,   j+1),
                            (i+1, j)
            ]:
                if  0 <= x < m and 0 <= y < n:
                    if matrix[i][j] > matrix[x][y]:
                        return False  
            return True
            
        for i in range(m):
            for j in range(n):
                if startcheck(i, j):
                    starts.append((i,j))
        @cache
        def dfs(i, j):
            result = 0
            for x, y in [
                            (i-1, j),
                (i,   j-1)          , (i,   j+1),
                            (i+1, j)
            ]:
                if  0 <= x < m and 0 <= y < n:
                    if matrix[i][j] < matrix[x][y]:
                        result = max(dfs(x, y), result)
            
            return result + 1
            
        result = 0
        for i, j in starts:
            result = max(dfs(i, j), result)
        return result
# @lc code=end


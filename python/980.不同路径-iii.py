#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        start = None
        zeros = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    zeros += 1
        
        path = set()
        def dfs(i, j):
            if grid[i][j] == 2:
                if len(path) == 2 + zeros:
                    return 1
                else:
                    return 0
            
            t = 0
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in path and grid[x][y] != -1:
                        path.add((x, y))
                        t += dfs(x, y)
                        path.remove((x, y))
            return t

        path.add(start)
        return dfs(start[0], start[1])
# @lc code=end
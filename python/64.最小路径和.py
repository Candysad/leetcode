#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        动态规划
        和 62. 的动态规划方法一致，只是每个格子加了权
        '''
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    grid[i][0] += grid[i-1][0]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # for line in grid:
        #     print(line)
        return grid[-1][-1]
            
            
# @lc code=end


#
# @lc app=leetcode.cn id=2923 lang=python3
#
# [2923] 找到冠军 I
#

# @lc code=start
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        winner = 0
        for i in range(n):
            if grid[i][winner]:
                winner = i
        
        return winner
        
        
        # teams = [0] * n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if grid[i][j]:
        #             teams[j] = 1
        #         else:
        #             teams[i] = 1

        # for i in range(n):
        #     if teams[i] == 0:
        #         return i
# @lc code=end


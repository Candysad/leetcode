#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        行列数字按顺序一样
        '''
        rows = {}
        for row in grid:
            t = ""
            for num in row:
                t += " " + str(num)
            rows[t] = rows.get(t, 0) + 1
        # print(rows)
        n = len(grid)
        result = 0
        for i in range(n):
            t = ""
            for j in range(n):
                t += " " + str(grid[j][i])         
            # print(t)
            result += rows.get(t, 0)
        
        return result
# @lc code=end


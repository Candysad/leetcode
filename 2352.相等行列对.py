#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        比的是对应位置数对应一样
        '''
        result = 0
        n = len(grid)
        row_sums = dict()
        for row in grid:
            row_sum = sum(row)   
            row_sums[row_sum] = row_sums.get(row_sum, 0) + 1
        
        print(row_sums)
        for i in range(n):
            column_sum = 0
            for j in range(n):
                column_sum += grid[j][i]
            print(column_sum)
            
            result += row_sums[column_sum]
        
        return result
# @lc code=end


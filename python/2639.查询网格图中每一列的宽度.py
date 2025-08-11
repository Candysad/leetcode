#
# @lc app=leetcode.cn id=2639 lang=python3
#
# [2639] 查询网格图中每一列的宽度
#

# @lc code=start
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        '''
        居然不如直接转字符串...
        '''
        m = len(grid)
        n = len(grid[0])
        result = [0] * n
        
        def length(num:int) -> int:
            if num == 0:
                return 1
            result = 1 if num < 0 else 0
            num = abs(num)
            while num:
                num //= 10
                result += 1
            return result
            
        
        for i in range(m):
            for j in range(n):
                result[j] = max(result[j], length(grid[i][j]))
        
        return result
# @lc code=end


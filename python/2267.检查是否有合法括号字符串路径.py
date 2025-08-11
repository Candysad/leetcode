#
# @lc app=leetcode.cn id=2267 lang=python3
#
# [2267] 检查是否有合法括号字符串路径
#
from functools import cache
# @lc code=start
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ')': return False
        
        m = len(grid)
        n = len(grid[0])
        
        @cache
        def dfs(b, i, j):
            if i == m or j == n: return False
            
            if grid[i][j] == '(':
                b += 1
            else:
                if b == 0:
                    return False
                else:
                    b -= 1

            if i == m-1 and j == n-1:
                return True if b == 0 else False
            return dfs(b, i + 1, j) or dfs(b, i, j + 1)
        
        return dfs(0, 0, 0)
# @lc code=end
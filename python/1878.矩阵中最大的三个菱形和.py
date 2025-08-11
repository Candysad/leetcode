#
# @lc app=leetcode.cn id=1878 lang=python3
#
# [1878] 矩阵中最大的三个菱形和
#

# @lc code=start
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        result = set()
        def rhombus(i, j):
            result.add(grid[i][j])
            
            for b in range(1, (m - 1 - i) // 2 + 1):
                if j - b < 0 or j + b >= n: break
                
                _sum = 0
                for t in range(b):
                    _sum += grid[i+t][j-t]
                    _sum += grid[i+b+t][j-b+t]
                    _sum += grid[i+2*b-t][j+t]
                    _sum += grid[i+b-t][j+b-t]
                
                result.add(_sum)
        
        for i in range(m):
            for j in range(n):
                rhombus(i, j)
        
        result = sorted((list(result)), reverse=True)[:3]
        return result
# @lc code=end
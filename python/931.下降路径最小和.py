#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                t = min(matrix[i-1][max(0, j-1) : min(n, j+2)])        
                matrix[i][j] += t
        
        return min(matrix[-1])
# @lc code=end


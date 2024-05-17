#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        for i in range(1, n-1):
            matrix[i][0] += min(matrix[i-1][0], matrix[i-1][1])
            matrix[i][-1] += min(matrix[i-1][-1], matrix[i-1][-2])
            for j in range(1, n-1):
                matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        
        matrix[-1][0] += min(matrix[-2][0], matrix[-2][1])
        matrix[-1][-1] += min(matrix[-2][-1], matrix[-2][-2])
        result = min(matrix[-1][0], matrix[-1][-1])
        for j in range(1, n-1):   
            result = min(matrix[-1][j] + min(matrix[-2][j-1], matrix[-2][j], matrix[-2][j+1]), result)

        return result
# @lc code=end


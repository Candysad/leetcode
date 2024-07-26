#
# @lc app=leetcode.cn id=311 lang=python3
#
# [311] 稀疏矩阵的乘法
#

# @lc code=start
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, t, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = []
        for i in range(m):
            line = []
            for j in range(n):
                line.append(sum(mat1[i][k] * mat2[k][j] for k in range(t)))
            result.append(line)
        
        return result
# @lc code=end
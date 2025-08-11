#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#

# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        
        result = [[0] * n for _ in range(m)]
        
        for j in range(n):
            for i in range(m):
                if colSum[j] > rowSum[i]:
                    colSum[j] -= rowSum[i]
                    result[i][j] = rowSum[i]
                    rowSum[i] = 0
                else:
                    result[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    break
        
        return result
# @lc code=end
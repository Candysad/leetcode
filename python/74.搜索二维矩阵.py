#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        t = [matrix[i][0] for i in range(n)]
        i = bisect_left(t, target)

        if i < n and matrix[i][0] == target:
            return True
        i -= 1
        if i == -1:
            return False
        
        j = bisect_left(matrix[i], target)
        if j < m and  matrix[i][j] == target:
            return True
        
        return False
# @lc code=end


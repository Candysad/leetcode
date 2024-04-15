#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        candidate = []
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][-1]:
                candidate.append(i)
        
        for i in candidate:
            index = bisect_left(matrix[i], target)
            if index < m and matrix[i][index] == target:
                return True
        
        return False
                
        
# @lc code=end


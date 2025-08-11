#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#
from heapq import *
# @lc code=start
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        queue = []
        for i in range(m):
            linepre = 0
            for j in range(n):
                t = matrix[i][j]
                if i > 0:
                    matrix[i][j] ^= matrix[i-1][j]
                matrix[i][j] ^= linepre
                
                heappush(queue, -matrix[i][j])
                linepre ^= t
        
        for i in range(k-1):
            heappop(queue)
        
        return -queue[0]
# @lc code=end


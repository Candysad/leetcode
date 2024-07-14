#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def check(num):
            i, j = n-1, 0
            result = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= num:
                    result += i + 1
                    j += 1
                else:
                    i -= 1
            return result
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + ((right - left) >> 1)
            c = check(mid)
            if c >= k:
                right = mid
            else:
                left = mid + 1
        return left    
# @lc code=end
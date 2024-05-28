#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        学会看数据范围选择方法
        '''
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            last = -1
            for j in range(n):
                if matrix[i][j] == '0':
                    last = j
                else:
                    length = j - last
                    dp[i][j] = length
                
                short = length 
                for k in range(i, -1, -1):
                    if dp[k][j] == 0:
                        break
                    short = min(short, dp[k][j])
                    result = max(result, short * (i-k+1))
        return result
# @lc code=end


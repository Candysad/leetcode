#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        动态规划简单题
        倒着想
        正着构建
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        status = [1, 2]
        for i in range(2, n):
            status.append(status[i-2] + status[i-1])
        
        return status[-1]
# @lc code=end
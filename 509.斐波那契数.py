#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        F = [0, 1]
        for i in range(2, n+1):
            F.append(F[i-2] + F[i-1])
        
        return F[-1]
        
# @lc code=end


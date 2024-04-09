#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        '''
        快速幂，不求余
        带符号的
        '''
        sign = 0
        if exponent < 0:
            sign = 1
            exponent = -exponent
        result = 1
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent >>= 1
        return 1/result if sign else result
        
        
# @lc code=end


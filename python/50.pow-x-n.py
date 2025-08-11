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
        esign = 1 if exponent > 0 else -1
        exponent = abs(exponent)
        
        result = 1
        now = base
        while exponent:
            if exponent & 1:
                result *= now
            now *= now
            exponent >>= 1
            
        return result if esign > 0 else 1 / result
# @lc code=end


#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#
from math import exp, log
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        偷鸡
        x^{0.5} = e^{0.5 * \ln x }
        '''
        if x == 0:
            return 0
        result = int(exp(0.5 * log(x)))
        if (result + 1) * (result + 1) <= x:
            return result + 1
        
        if result * result > x:
            return result - 1
        
        return result
        
        
        '''
        二分
        '''
        # left , right = 1, x
        # while left <= right:
        #     mid = (left + right) // 2
        #     p = mid * mid
        #     if p < x:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return left if left * left <= x else left - 1

# @lc code=end


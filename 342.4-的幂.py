#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        数学特征
        4的幂除3余1，且是2的幂
        '''
        # if n > 0 and n & (n-1) == 0 and n % 3 == 1:
        #     return True
        # return False
    
        '''
        2进制特征
        4的幂是2的2的倍数幂 4^x = 2^{2y}
        4 = 2**2 = 100
        16 = 2**4 = 10000
        即一定是1为首其余位为0且0有偶数个
        '''
        if n <= 0:
            return False
        
        while n > 1:
            if n >> 2 << 2 != n:
                return False
            n = n >> 2
        return True
        
        
# @lc code=end


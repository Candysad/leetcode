#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        '''
        移到最后一位
        '''
        # while n != 1:
        #     if n >> 1 << 1 != n:
        #         return False
        #     n = n >> 1
        # return True
        
        '''
        2进制特性
        2的幂总是以1开始剩余位为0
        10000
        它减1得
        01111
        两数取与得0
        '''
        
        if n & (n-1) == 0:
            return True
        
        return False
        
# @lc code=end


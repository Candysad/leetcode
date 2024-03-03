#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        '''
        直接数
        线性时间
        '''
        # flag = n % 2
        # n = n >> 1
        # while n:
        #     if flag == n % 2:
        #         return False
        #     flag = n % 2
        #     n = n >> 1
        # return True
        
        '''
        用 11(3) 判断最后两位
        11 或 00 则重复 
        '''
        while n:
            if n & 3 == 3 or n & 3 == 0:
                return False
            n = n >> 1
        return True      
# @lc code=end
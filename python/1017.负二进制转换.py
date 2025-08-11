#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        
        result = ''
        while n:
            t = n % -2
            n //= 2
            result+=str(abs(t))
            if t == -1:
                n += 1
        return result
            
            
# @lc code=end


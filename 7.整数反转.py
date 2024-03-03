#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
max_ = 2147483647
min_ = 2147483648
class Solution:
    def reverse(self, x: int) -> int:
        '''
        字符串倒转
        '''
    #     flag = 0 if x >= 0 else 1 # 符号
    #     x = str(x) if flag == 0 else str(x)[1:]
    #     x = [x[i] for i in range(len(x)-1, -1, -1)]
    #     x = int(''.join(x))
    #     if (x > max_ and flag == 0) or (x > min_ and flag):
    #         return 0
        
    #     return x if flag == 0 else -x
    
    
        '''
        十进制退位
        '''
        result = 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        
        while x > 0:
            result = result * 10 +  (x % 10)
            x = x // 10
            
        if (flag == -1 and result > min_) or result > max_:
            return 0
        else:
            return result * flag
    
# @lc code=end


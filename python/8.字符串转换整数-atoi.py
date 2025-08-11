#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
max_ = 2147483647
min_ = 2147483648
class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        十进制按位添加
        判断范围
        '''
        s = s.strip()
        print(s)
        if len(s) == 0:
            return 0
        
        def check(num, flag):
            if (flag == -1 and num >= min_):
                return min_ * flag
            if num >= max_:
                return max_ * flag
            return True
        
        i = 0
        result = 0
        flag = 1
        numbers = '0123456789'
        replace_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-+ '
          
        # 符号
        if s[i] == '-':
            flag = -1
            i += 1
        elif s[i] == '+':
            i += 1
        elif s[i] in numbers:
            result = int(s[i])
            i += 1
        else:
            return 0
        
        while i < len(s):
            if s[i] in replace_list:
                return result * flag
            
            result = result * 10 + int(s[i])
            t = check(result, flag)
            if t != True:
                return t
            
            i += 1 
        return result * flag     
# @lc code=end


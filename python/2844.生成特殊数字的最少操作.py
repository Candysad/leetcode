#
# @lc app=leetcode.cn id=2844 lang=python3
#
# [2844] 生成特殊数字的最少操作
#
from math import inf
# @lc code=start
class Solution:
    def minimumOperations(self, num: str) -> int:
        # 00 25 50 75
        n = len(num)
        c0 = num.count('0')
        result = n - 1 if c0 else n
        
        f0 = -1
        f5 = -1
        l0, l2, l7, l5 = -1, -1 , -1, -1
        
        for i in range(n-1, -1, -1):
            c = num[i]
            if c == '0':
                if f0 == -1: f0 = i
                elif l0 == -1: l0 = i
            
            elif c == '5':
                if f5 == -1:
                    f5 = i
                    
                if f0 != -1 and l5 == -1:
                    l5 = i
            
            elif c == '7' and l7 == -1 and f5 != -1:
                l7 = i
            
            elif c == '2' and l2 == -1 and f5 != -1:
                l2 = i
        
        r00 = inf
        if f0 != -1 and l0 != -1:
            r00 = n - l0 - 2
        
        r25 = inf
        if l2 != -1 and f5 != -1:
            r25 = n - l2 - 2
        
        r75 = inf
        if l7 != -1 and f5 != -1:
            r75 = n - l7 - 2
        
        r50 = inf 
        if l5 != -1 and f0 != -1:
            r50 = n - l5 - 2
        
        return min(result, r00, r25, r50, r75)
# @lc code=end
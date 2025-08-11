#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        单调栈
        '''
        n = len(num)
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            
            stack.append(c)
        
        if k > 0:
            stack = stack[:-k]
        result = ''.join(stack).lstrip('0')
        
        return result if result != '' else '0'
# @lc code=end


#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        栈
        '''
        left = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        # right = [']', ')', '}']
        stack = []
        
        for bracket in s:
            if bracket in left.keys(): # 左括号入栈
                stack.append(bracket)
            else:
                if stack:
                    if bracket != left[stack.pop()]: # 右括号和栈顶比较
                        return False
                else:
                    return False
            
        if stack: # 没匹配完
            return False
        
        return True
        
# @lc code=end


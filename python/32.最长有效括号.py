#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        span = [] # 左端点，右端点
        
        def addspan(left, right):
            if span:
                # (...)(...)
                if span[-1][1] + 1 == left:
                    span[-1][1] = right
                    if len(span) > 1:
                        left, right = span.pop()
                        addspan(left, right)
                    return
                # ((...))
                if span[-1][0] - 1 == left:
                    span.pop()
                    if span:
                        addspan(left, right)
                        return
                
            span.append([left, right])
            return
                
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack: # 栈里只会留左括号，空了说明这个右括号非法
                    left, right = stack.pop(), i # 记录新的区间的左右
                    addspan(left, right)
        result = 0
        for left, right in span:
            result = max(right - left + 1, result)
        return result
                        
                    
                    
        
        
# @lc code=end


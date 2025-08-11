#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#
from operator import and_, or_, 
from functools import reduce

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def ands(items:list):
            return reduce(and_, items)

        def ors(items:list):
            return reduce(or_, items)
        
        def nos(items:bool):
            return not items[0]
        
        def ops(c:str, items:list):
            if c == '&': return ands(items)
            elif c == '|': return ors(items)
            return nos(items)
        
        def decode(item):
            if item == 't': return True
            return False      
        
        stack = []
        for i, c in enumerate(expression):
            if c in 'tf':
                stack.append(decode(c))
            elif c in '!&|':
                stack.append(c)
            elif c == ')':
                vals = []
                while type(stack[-1]) == type(True):
                    vals.append(stack.pop())      
                stack.append(ops(stack.pop(), vals))
        
        return stack[-1]
# @lc code=end
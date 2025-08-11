#
# @lc app=leetcode.cn id=439 lang=python3
#
# [439] 三元表达式解析器
#

# @lc code=start
class Solution:
    def parseTernary(self, expression: str) -> str:
        n = len(expression)
        ops = []
        i = n-1
        while i >= 0:
            c = expression[i]
            if c != '?' and c != ':':
                ops.append(c)
            elif c== '?':
                i -= 1
                c = expression[i]
                op1 = ops.pop()
                op2 = ops.pop()
                if c == 'T':
                    ops.append(op1)
                else:
                    ops.append(op2)
            i -= 1
        return ops[0]
# @lc code=end
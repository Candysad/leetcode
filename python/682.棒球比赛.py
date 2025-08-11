#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == '+':
                op1 = stack[-2]
                op2 = stack[-1]
                stack.append(op1 + op2)
            elif c == 'D':
                stack.append(2 * stack[-1])
            elif c == 'C':
                stack.pop()
            else:
                stack.append(int(c))

        return sum(stack) 
# @lc code=end
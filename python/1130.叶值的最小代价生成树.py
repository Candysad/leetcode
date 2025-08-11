#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
#
from math import inf
# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        result = 0
        for num in arr:
            while stack and stack[-1] <= num:
                pre = stack.pop()
                if not stack or stack[-1] > num:
                    result += pre * num
                else:
                    result += stack[-1] * pre
            stack.append(num)
        
        while len(stack) > 1:
            pre = stack.pop()
            result += stack[-1] * pre
        return result
# @lc code=end
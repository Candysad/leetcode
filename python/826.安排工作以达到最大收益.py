#
# @lc app=leetcode.cn id=826 lang=python3
#
# [826] 安排工作以达到最大收益
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit), key=lambda x:x[0])
        
        stack = [[jobs[0][0], jobs[0][1]]]
        for d, p in jobs:
            if d == stack[-1][0]:
                stack[-1][1] = max(stack[-1][1], p)
            else:
                stack.append([d, max(stack[-1][1], p)])

        result = 0
        for w in worker:
            if w < stack[0][0]: continue
            
            elif w > stack[-1][0]:
                result += stack[-1][1]
                
            else:
                i = bisect_left(a=stack, x=w, key=lambda x:x[0])
                result += stack[i-1][1] if w < stack[i][0] else stack[i][1]
                
        return result
# @lc code=end


#
# @lc app=leetcode.cn id=346 lang=python3
#
# [346] 数据流中的移动平均值
#
from collections import deque
# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        self.stack = deque([0])
        self.size = size

    def next(self, val: int) -> float:
        stack = self.stack
        size = self.size
        stack.append(val + stack[-1])
        if len(stack) > size + 1:
            stack.popleft()
    
        return (stack[-1] - stack[max(0, len(stack) - 1 - size)]) / (len(stack) - 1)

# @lc code=end


#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
from heapq import *
from collections import defaultdict

# @lc code=start
class MinStack:
    '''
    栈 + 记录最小的栈
    '''
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mins:
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)
        
        
    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

    '''
    栈 + 最小堆 + 出栈记录
    '''
    # def __init__(self):
    #     self.stack = []
    #     self.queue = []
    #     self.out = defaultdict(int)

    # def push(self, val: int) -> None:
    #     heappush(self.queue, val)
    #     self.stack.append(val)
        
    # def pop(self) -> None:
    #     self.out[self.stack.pop()] += 1

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     while self.out[self.queue[0]]:
    #         self.out[heappop(self.queue)] -= 1
    #     return self.queue[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


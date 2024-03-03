#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:
    def __init__(self):
        self.stack = []
        self.now = 0
        self.max_length = 0


    def push(self, x: int) -> None:
        if self.now == self.max_length:
            self.stack.append(x)
            self.now += 1
            self.max_length += 1
        elif self.now < self.max_length:
            self.stack[self.now] = x
            self.now += 1


    def pop(self) -> int:
        self.now -= 1
        return self.stack[self.now]


    def top(self) -> int:
        return self.stack[self.now-1]

    def empty(self) -> bool:
        return self.now == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end


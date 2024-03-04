#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    '''
    python 没有栈，不适合这题
    '''
    # def __init__(self):
    #     self.frontlist = []
    #     self.backlist = []
    #     self.length = 0

    # def push(self, x: int) -> None:
    #     self.frontlist.append(x)
    #     self.length += 1

    # def pop(self) -> int:
    #     self.backlist = [self.frontlist[i] for i in range(len(self.frontlist)-1, len(self.frontlist) - self.length - 1, -1)]
    #     self.length -= 1
    #     return self.backlist[-1]


    # def peek(self) -> int:
    #     self.backlist = [self.frontlist[i] for i in range(len(self.frontlist)-1, len(self.frontlist) - self.length - 1, -1)]
    #     return self.backlist[-1]


    # def empty(self) -> bool:
    #     return self.length == 0
    
    '''
    直接用list实现一个
    实际时间和栈模拟的一样😓
    '''
    def __init__(self):
        self.list = []
        self.length = 0
        self.head = 0

    def push(self, x: int) -> None:
        self.list.append(x)
        self.length += 1

    def pop(self) -> int:
        self.length -= 1
        self.head += 1
        return self.list[self.head - 1]


    def peek(self) -> int:
        return self.list[self.head]


    def empty(self) -> bool:
        return self.length == 0
    



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


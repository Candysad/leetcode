#
# @lc app=leetcode.cn id=2069 lang=python3
#
# [2069] 模拟行走机器人 II
#

# @lc code=start
class Robot:

    def __init__(self, width: int, height: int):
        self.pos = 0 # [0, 2 * w + 2 * h - 4 - 1]
        self.limit = (width, height)
        self.started = False

    def step(self, num: int) -> None:
        w, h = self.limit
        self.pos = (self.pos + num) % (2 * w + 2 * h - 4)
        if not self.started:
            self.started = True

    def getPos(self) -> List[int]:
        w, h = self.limit
        pos = self.pos
        if pos <= w - 1:
            x = pos
            y = 0
        elif pos <= w + h - 2:
            x = w - 1
            y = pos - w + 1
        elif pos <= 2 * w + h - 3:
            x = w-1 - (pos - w - h + 2)
            y = h - 1 
        else:
            x = 0
            y = 1 + (2 * w + 2 * h - 4 - 1 - pos)
        return [x, y]

    def getDir(self) -> str:
        if not self.started: return 'East'
        
        w, h = self.limit
        pos = self.pos
        
        if 0 < pos <= w - 1:
            return 'East'
        elif w - 1 < pos <= w + h - 2:
            return 'North'
        elif w + h - 2 < pos <= 2 * w + h - 3:
            return 'West'
        else:
            return 'South'
# @lc code=end
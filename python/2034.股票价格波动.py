#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] 股票价格波动
#
from heapq import *
from collections import defaultdict
# @lc code=start
class StockPrice:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.table = defaultdict(int)
        self.now = [0, 0]
        

    def update(self, timestamp: int, price: int) -> None:
        self.table[timestamp] = price
        heappush(self.maxheap, [-price, timestamp])
        heappush(self.minheap, [price, timestamp])
        if timestamp >= self.now[0]:
            self.now = [timestamp, price]

    def current(self) -> int:
        return self.now[1]


    def maximum(self) -> int:
        while self.maxheap[0][0] != -self.table[self.maxheap[0][1]]:
            heappop(self.maxheap)

        return -self.maxheap[0][0]

    def minimum(self) -> int:
        while self.minheap[0][0] != self.table[self.minheap[0][1]]:
            heappop(self.minheap)
        return self.minheap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end
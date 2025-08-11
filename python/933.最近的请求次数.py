#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#
from bisect import bisect_left
# @lc code=start
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        left = bisect_left(self.queue, t-3000)
        result = len(self.queue) - left
        self.queue = self.queue[left:]
        return result
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
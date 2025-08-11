#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
from bisect import bisect_left
# @lc code=start
class MedianFinder:
    '''
    二分直接更新所有数
    '''
    def __init__(self):
        self.nums = []
        self.length = -1


    def addNum(self, num: int) -> None:
        i = bisect_left(self.nums, num)
        self.nums.insert(i, num)
        self.length += 1


    def findMedian(self) -> float:
        i = self.length // 2
        if (self.length+1) % 2:
            return self.nums[i] / 1
        else:
            return (self.nums[i] + self.nums[i+1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end


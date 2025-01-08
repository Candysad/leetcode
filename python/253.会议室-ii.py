#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#
from itertools import accumulate
# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count = [0] * (max(intervals, key=lambda x: x[1])[1] + 1)        
        for a, b in intervals:
            count[a] += 1
            count[b] -= 1
        
        return max(list(accumulate(count)))
# @lc code=end
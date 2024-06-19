#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        l, r = -1, -1
        result = []
        for left, right in intervals:
            if left > r:
                result.append([l, r])
                l, r = left, right
            elif left <= r:
                r = max(r, right)
            
        result.append([l, r])
        return result[1:]
# @lc code=end
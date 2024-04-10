#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        intervals.append(None)
        
        result = []
        last = intervals[0]
        for span in intervals[1:]:
            if span == None:
                result.append(last)
                return result
            if  last[0] <= span[0] <= last[1]:
                last = [last[0], max(last[1], span[1])]
            else:
                result.append(last)
                last = span
        return result
        
# @lc code=end


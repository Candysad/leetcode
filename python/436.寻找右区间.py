#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        spans = sorted([(i, span[0], span[1]) for i, span in enumerate(intervals)], key=lambda x:x[1])
        result = [-1] * n
        for i, (index, start, end) in enumerate(spans):
            if start == end:
                result[index] = index
                continue
            
            j = bisect_left(a=spans, x=end, lo=i+1, key=lambda x: x[1])
            if j == n:
                continue
            else:
                result[index] = spans[j][0]
        
        return result
# @lc code=end


#
# @lc app=leetcode.cn id=1272 lang=python3
#
# [1272] 删除区间
#

# @lc code=start
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        for left, right in intervals:
            if left < toBeRemoved[0] and toBeRemoved[0] < right <= toBeRemoved[1]:
                result.append([left, toBeRemoved[0]])

            elif toBeRemoved[0] <= left <= toBeRemoved[1] and right > toBeRemoved[1]:
                result.append([toBeRemoved[1], right])
            
            elif left >= toBeRemoved[1] or right <= toBeRemoved[0]:
                result.append([left, right])
            
            elif left <= toBeRemoved[0] and right > toBeRemoved[1]:
                result.append(left, toBeRemoved[0])
                result.append(toBeRemoved[0], right)
            
        return result
# @lc code=end


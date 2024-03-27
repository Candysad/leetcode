#
# @lc app=leetcode.cn id=2580 lang=python3
#
# [2580] 统计将重叠区间合并成组的方案数
#

# @lc code=start
mod = 10**9 + 7
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        result = 2
        last_right = ranges[0][1]
        
        for span in ranges:
            if last_right >= span[0]:
                last_right = max(last_right, span[1])
            else:
                result = result * 2 % mod
                last_right = span[1]
        
        return  result
# @lc code=end


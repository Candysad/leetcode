#
# @lc app=leetcode.cn id=2960 lang=python3
#
# [2960] 统计已测试设备
#

# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        
        for b in batteryPercentages:
            if b - result > 0:
                result += 1
        
        return result
# @lc code=end


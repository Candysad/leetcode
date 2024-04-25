#
# @lc app=leetcode.cn id=2739 lang=python3
#
# [2739] 总行驶距离
#

# @lc code=start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # result = 0
        # while mainTank >= 5 and additionalTank:
        #     mainTank -= 4
        #     result += 5
        #     additionalTank -= 1
        
        # if mainTank > 0:
        #     result += mainTank
        
        # return result * 10
        
        n = min((mainTank - 5) // (5-1) + 1, additionalTank) if mainTank >= 5 else 0
        return 10 * (n + mainTank)
        
# @lc code=end


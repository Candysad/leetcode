#
# @lc app=leetcode.cn id=2798 lang=python3
#
# [2798] 满足目标工作时长的员工数目
#

# @lc code=start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum([1 if h >= target else 0 for h  in hours])
# @lc code=end


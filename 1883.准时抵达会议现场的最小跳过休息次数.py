#
# @lc app=leetcode.cn id=1883 lang=python3
#
# [1883] 准时抵达会议现场的最小跳过休息次数
#

# @lc code=start
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1
        
        n = len(dist)
        
        '''
        正着想
            从i出发要花的时间，返回后面的时间消耗和最少休息次数
            但是每次出发要看前一次的结束时间是否是整数
        反过来
            从后往前找来确定出发时间是整数
            
        时间变成路程，来避免分数运算
        '''

            
# @lc code=end


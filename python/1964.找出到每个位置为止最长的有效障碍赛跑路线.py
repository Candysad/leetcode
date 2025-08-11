#
# @lc app=leetcode.cn id=1964 lang=python3
#
# [1964] 找出到每个位置为止最长的有效障碍赛跑路线
#
from bisect import bisect_right
# @lc code=start
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        '''
        300.找最长递增序列长度 的变种
        之前只找最长的
        现在找以每个位置为结尾的最长的，相当于多套一层遍历，或者说每一步维护之后都记录一下当前最长
        
        result[i] 以当前为结尾的最长序列的长度
        dp[i] 有i那么长的序列的末尾元素
        每次去obs里二分查一下当前能插进去的位置，就得到当前ob能做结尾的序列长度
        '''
        dp = []
        result = []
        for ob in obstacles:
            index = bisect_right(dp, ob)
            if index == len(dp):
                dp.append(ob)
            else:
                dp[index] = ob
            result.append(index+1)
        return result
        
        
# @lc code=end


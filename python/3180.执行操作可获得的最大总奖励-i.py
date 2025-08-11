#
# @lc app=leetcode.cn id=3180 lang=python3
#
# [3180] 执行操作可获得的最大总奖励 I
#

# @lc code=start
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        '''
        (1 << num) 巧妙地选出了所有小于 num 的数
        做按位与即可选出
        '''
        rewardValues.sort()
        dp = 1
        
        for num in rewardValues:
            lower = (1 << num) - 1
            lower = dp & lower
            dp |= lower << num
        return dp.bit_length() - 1
# @lc code=end
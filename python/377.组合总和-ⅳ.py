#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        不限次数，完全背包
        不同顺序算不同答案，所以coin遍历在内层
        '''
        dp = [1] + [0] * target
        nums.sort()
        
        for i in range(1, target+1):
            for coin in nums:
                if coin > i: break
                dp[i] += dp[i-coin]
        return dp[-1]
# @lc code=end
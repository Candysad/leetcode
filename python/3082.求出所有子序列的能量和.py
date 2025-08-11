#
# @lc app=leetcode.cn id=3082 lang=python3
#
# [3082] 求出所有子序列的能量和
#

# @lc code=start
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        
        dp = [1] + [0] * k
        for num in nums:
            for i in range(k, -1, -1):
                dp[i] = dp[i] + dp[i] # 外层不选内层不选 + 外层选内层不选
                dp[i] += dp[i-num] if i >= num else 0    # 外层选内层选
                dp[i] %= mod
        return dp[-1]
# @lc code=end
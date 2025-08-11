#
# @lc app=leetcode.cn id=1589 lang=python3
#
# [1589] 所有排列中的最大和
#

# @lc code=start
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        dp = [0] * (n+1)
        for left, right in requests:
            dp[left] += 1
            dp[right+1] -= 1
        
        now = 0
        t = []
        for d in dp[:-1]:
            now += d
            t.append(now)
        
        t = sorted(zip(t, range(n)))
        nums.sort()
        result = 0
        for i in range(n):
            result += nums[i] * t[i][0]
            result %= mod
        return result
        
        
# @lc code=end
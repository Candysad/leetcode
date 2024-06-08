#
# @lc app=leetcode.cn id=1458 lang=python3
#
# [1458] 两个子序列的最大点积
#
from math import inf
# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[-inf] * (n+1) for _ in range(m+1)]
        result = -inf
        for i in range(1, m+1):
            for j in range(1, n+1):
                x = nums1[i-1]*nums2[j-1]
                dp[i][j] = max(dp[i-1][j-1] + x, dp[i-1][j], dp[i][j-1], x)
        return dp[-1][-1]
# @lc code=end


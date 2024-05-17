#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _1 in range(n+1)] for _2 in range(m+1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                carry = 1 if nums1[i-1] == nums2[j-1] else 0
                dp[i][j] = max(dp[i-1][j-1] + carry, dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
# @lc code=end


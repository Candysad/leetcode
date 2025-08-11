#
# @lc app=leetcode.cn id=1186 lang=python3
#
# [1186] 删除一次得到子数组最大和
#
from math import inf
# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0, 0] for _ in range(n+1)]
        
        allmin = True
        result = -inf
        for i in range(1, n+1):
            num = arr[i+1]
            if num >= 0: allmin = True
            
            if dp[i-1][0] >= 0:
                dp[i][0] = dp[i-1][0] + num
            else:
                dp[i][0] = num
            
            if num < 0:
                dp[i][1] = max(dp[i-1][1] + num, dp[i][0] - num)
            else:
                dp[i][1] = dp[i-1][1] + num
            
            result = max(result, dp[i][0], dp[i][1])
        
        if allmin:
            return max(arr)
        return result
# @lc code=end


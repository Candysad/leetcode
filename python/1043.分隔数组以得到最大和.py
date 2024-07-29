#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#
from collections import deque
# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = deque([0])
        pres = deque([0])
        
        for num in arr:
            lastmax = num
            result = dp[-1] + lastmax
            dn = len(dp)
            
            for j in range(dn - 1, 0, -1):
                lastmax = max(lastmax, pres[j])
                result = max(result, dp[j-1] + lastmax * (dn - j + 1))
            
            dp.append(result)
            pres.append(num)
            if dn + 1 == k + 1:
                dp.popleft()
                pres.popleft()
            
        return dp[-1]
# @lc code=end
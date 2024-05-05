#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#
from bisect import bisect_right
# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        '''
        每个工作都要在上一个工作结束之后才能开始
        startTime[i] >= endTime[j]
        按照 endTime 排序方便找所有前面的工作
        '''
        times = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        '''
        dp[i] 前 i 个工作不管具体怎么选，能够获得的最大收益
        '''
        dp = [0] * (n+1)
        
        for j in range(1, n + 1):
            i = j - 1 #
            # 不选当前工作
            dp[j] = dp[j-1]
            
            # 选当前工作
            # 找上一个能选的位置
            pre = bisect_right(a=times, x=times[i][0], hi=i, key= lambda x: x[1])
            dp[j] = max(dp[j], dp[pre] + times[i][2])
            
        return dp[-1]
# @lc code=end


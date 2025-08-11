#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
from math import inf
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''
        二分
        '''
        def check(limit):
            '''
            按照limit上限分组，返回分组数
            分组数太多说明limit太小
            分组数太少说明limit太大
            '''
            result = 1
            _sum = 0
            for n in nums:
                if _sum + n > limit:
                    result += 1
                    _sum = n
                else:
                    _sum += n
            return result
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            c = check(mid)
            if c > k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
        
        '''
        DP
        '''
        # n = len(nums)
        # dp = [[inf] * k for _ in range(n)]
        # tsum = 0
        # for j, num in enumerate(nums):
        #     tsum += num
        #     dp[j][0] = tsum
            
        # for i in range(1, k):
        #     for j in range(i, n):
        #         for t in range(0, j):
        #             dp[j][i] = min(dp[j][i], max(dp[t][i-1], dp[j][0] - dp[t][0]))

        # return dp[-1][-1]
# @lc code=end


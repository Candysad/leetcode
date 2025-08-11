#
# @lc app=leetcode.cn id=2771 lang=python3
#
# [2771] 构造最长非递减子数组
#
from functools import cache
# @lc code=start
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        动态规划
        '''
        nums1, nums2 = [0] + nums1, [0] + nums2
        n = len(nums1)
        dp = [[0,0]] + [[1, 1] for _ in range(n-1)] # 到此处为止选择了此处（0:nums1， 1:nums2）的最长长度
        for i in range(1, n):
            num1, num2 = nums1[i], nums2[i]
            pre1, pre2 = nums1[i-1], nums2[i-1]
            
            if num1 >= pre1:
                dp[i][0] = dp[i-1][0] + 1
            if num1 >= pre2:
                dp[i][0] = max(dp[i-1][1] + 1, dp[i][0])
            
            if num2 >= pre1:
                dp[i][1] = dp[i-1][0] + 1
            if num2 >= pre2:
                dp[i][1] = max(dp[i-1][1] + 1, dp[i][1])
        return max(max(dp, key=lambda x:max(x[0], x[1])))
        
        '''
        dfs
        '''
        # n = len(nums1)
        # @cache
        # def dfs(i, last):
        #     if i == n:
        #         return 0, 0
            
        #     num1, num2 = nums1[i], nums2[i]
        #     if num1 >= last and num2 >= last:
        #         t = dfs(i+1, min(num1, num2))
        #         return t[0] + 1, t[1]
        #     elif num1 < last and num2 < last:
        #         t = dfs(i+1, min(num1, num2))
        #         return 0, max(t[0]+1, t[1])
        #     else:
        #         _min, _max = (num1, num2) if num1 < num2 else (num2, num1)
        #         t1 = dfs(i+1, _min)
        #         t2 = dfs(i+1, _max)

        #         return t2[0] + 1, max(t1[0] + 1, t1[1], t2[1])
        
        # return max(dfs(0, 0))
# @lc code=end


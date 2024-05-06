#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        动态规划
        状态 开头到当前位置最长子序列的长度，包含第i位
        转移 对于i，找能用i增长的最长序列 
        '''
        n = len(nums)
        if n == 1:
            return 1
        
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
        '''
        贪心
        记录每个长度最小的末尾元素
        新出现一个更大的数，按顺序按大小都该增加一个在后面延长一位
        后续新出现的元素总比前面某个位置的末尾元素大，比谁大，就是替换谁的位置
        '''
        # n = len(nums)
        # if n == 1:
        #     return 1
        
        # d = [nums[0]]
        # for i in range(1, n):
        #     now = nums[i]
        #     # print(d, now)
        #     if now > d[-1]:
        #         d.append(now)
        #     else:
        #     # 二分法
        #         left, right = 0, len(d)-1
        #         p = right
        #         while left <= right:
        #             # print(left, right, p)
        #             mid = (left + right) // 2
        #             if d[mid] >= now:
        #                 p = mid
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
        #         d[p] = now
        # return len(d)
# @lc code=end


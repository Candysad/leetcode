#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        动态规划
        状态 到当前i位置结束的最长递增子序列长度, 该长度子序列在此处结束的出现次数
        转移 遍历 0..i-1 检查i可否递增并记录重复的次数
        '''
        n = len(nums)
        if n == 1:
            return 1
        
        dplength = [1 for i in range(n)]
        dpcount = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dplength[i] < dplength[j] + 1:
                        dplength[i] = dplength[j] + 1
                        dpcount[i] = dpcount[j]
                    elif dplength[i] == dplength[j] + 1:
                        dpcount[i] += dpcount[j]
        
        max_len = max(dplength)
        # print(dplength)
        # print(dpcount)
        return sum(dpcount[i] if dplength[i] == max_len else 0 for i in range(n))
        
        '''
        贪心
        '''
    
# @lc code=end


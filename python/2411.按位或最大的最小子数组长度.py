#
# @lc app=leetcode.cn id=2411 lang=python3
#
# [2411] 按位或最大的最小子数组长度
#
# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        '''
        这道题问的是以i为左侧的最短最大ors，所以只有从右边往左边走，走到i就存一个答案
        现在起点其实是在右侧，相当于i是固定的终点
        用数组或字典，存右侧开始每一位起点到当前终点i的(或值：右端的起点位置)
        如果更左侧的右端点或过来得到的值之前已经出现，那么之前记录的 右端起点位置一定比现在的更远，所以更新
        python字典第一个进来的会放在最开始，也就是当前或值最大的
        '''
        n = len(nums)
        result = []
        dp = {}
        for i in range(n-1, -1, -1):
            num = nums[i]
            dp = {ors | num : right_index for ors, right_index in dp.items()} # 遍历一遍更新当前的所有ors
            dp[num] = i # 把自己放进来，别的值都和自己或过了，应该都大于等于自己
                        # 如果有重复值，当前的下标更靠左，结果更短
            
            right = i
            for _, right_index in dp.items():
                right = right_index
                break
            result.append(right - i + 1)
        
        return result[::-1]
# @lc code=end


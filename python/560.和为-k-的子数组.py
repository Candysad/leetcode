#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        动态规划
        爆内存了...😓
        '''
        # n = len(nums)
        # if n  == 1:
        #     if nums[0] == k:
        #         return 1
        #     else:
        #         return 0
            
        # dp = [[0 if i != j else nums[i] for i in range(n)] for j in range(n)]
        # result = 0
        # for left in range(n):
        #     if dp[left][left] == k:
        #         result += 1
        #     for right in range(left+1, n):
        #         dp[left][right] = dp[left][right-1] + nums[right]
        #         if dp[left][right] == k:
        #             result += 1
        # return result

        '''
        遍历连续元素的组合不够快，没有存储和这个概念
        保留前面出现的和，用当前位置的和减去前面位置的和找区间和是否满足
        '''
        n = len(nums)
        if n  == 1:
            if nums[0] == k:
                return 1
            else:
                return 0
            
        pres = {0:1} # 记录空的为 0
        result = 0
        now = 0
        for i in range(n):
            now += nums[i]
            result += pres.get(now-k, 0)
            pres[now] = pres.get(now, 0) + 1
        
        return result
# @lc code=end


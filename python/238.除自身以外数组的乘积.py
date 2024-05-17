#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        以不要的位置为分界，算两边的乘积再乘在一起
        左边存在result里，右边从右向左一次遍历记录，只需要开一个变量
        '''
        n = len(nums)
        result = [1] * n
        result[0] = nums[0]
        for i in range(1, n):
            result[i] = result[i-1] * nums[i]
        
        right = 1
        for i in range(n-1, 0, -1):

            result[i] = result[i-1] * right
            
            right *= nums[i]
        result[0] = right
        
        return result
        
        '''
        子数组排序
        回溯
        超时...😓
        '''
        # n = len(nums)
        # result = [0]*n
        
        # def dfs(prod, absent, i, layer):
        #     if layer == n:
        #         if absent != -1:
        #             result[absent] = prod
        #         return
            
        #     dfs(prod*nums[i], absent, i+1, layer+1) # +1
            
        #     if absent == -1:
        #         dfs(prod, i, i+1, layer+1) # 缺自己
            
        # dfs(1,-1, 0, 0)
        # return result
# @lc code=end


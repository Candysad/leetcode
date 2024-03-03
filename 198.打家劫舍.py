#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return nums[0] if nums[0] > nums[1] else nums[1]
        
        # # 记录的是到当前位置能得到的最高的值
        # nums[1] = nums[0] if nums[0] > nums[1] else nums[1]
        # for i in range(2, len(nums)):
        #     nums[i] = max(nums[i]+ nums[i-2], nums[i-1])
        
        # return nums[len(nums)-1]
        
        '''
        代码简化
        易读性差
        '''
        left = right = 0
        for n in nums:
            left, right = right, max(left + n, right) 
            '''
            左
                right 本来是上次的最大值，更新为当前能偷到的最大值
                left  本来是上上次的最大值，更新为上一次的最大值
            右
                left + n 为上上次最大值 + 这次偷
                right    为上次的最大值 + 这次不偷
            '''
        return right
# @lc code=end


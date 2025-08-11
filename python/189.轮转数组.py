#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        向右走k下，即0变成k
        此时前面空出来k个位置，用来放后k个数
        '''
        # 考虑k超过了一圈
        length = len(nums)
        k %= length
        
        nums[:] = nums[-k:] + nums[0:-k]
        
# @lc code=end


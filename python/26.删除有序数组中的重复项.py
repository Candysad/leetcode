#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        left = right = 0
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            
            if right < len(nums):
                left += 1
                nums[left] = nums[right]
            
        return left + 1
# @lc code=end


#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # O(logn)
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            k = len(nums)-1
            for j in range(i+1, len(nums)-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[i] + nums[j] > -nums[k]:
                    k -= 1
                if j == k:
                    break
                
                if nums[i] + nums[j] == -nums[k]:
                    result.append([nums[i], nums[j], nums[k]])
        return result
            
# @lc code=end


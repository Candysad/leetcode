#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # O(logn)
        min_diff = target - (nums[0] + nums[1] + nums[len(nums)-1])
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            k = len(nums)-1
            for j in range(i+1, len(nums)-1):
                if j > i + 1 and j < k - 1 and nums[j] == nums[j-1]:
                    continue
                if j < k - 1 and (nums[i] + nums[j] +nums[k]) < target:
                    continue
                
                while j < k - 1 and (nums[i] + nums[j] +nums[k]) > target:
                    k -= 1
                if abs(target - (nums[i] + nums[j] + nums[k])) < abs(min_diff):
                    min_diff = target - (nums[i] + nums[j] + nums[k])
                
                if j == k-1:
                    break
                    
        return target - min_diff
# @lc code=end


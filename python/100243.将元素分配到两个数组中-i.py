#
# @lc app=leetcode.cn id=100243 lang=python3
#
# [100243] 将元素分配到两个数组中 I
#

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        stack1 = [nums[0]]
        stack2 = [nums[1]]
        i = 2
        while i < len(nums):
            if stack1[-1] > stack2[-1]:
                stack1.append(nums[i])
            else:
                stack2.append(nums[i])
            i += 1
        
        nums[::] = stack1 + stack2
        return nums 
# @lc code=end
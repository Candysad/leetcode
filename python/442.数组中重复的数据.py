#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                result.append(num)
            else:
                nums[num-1] *= -1
                
        return result
# @lc code=end


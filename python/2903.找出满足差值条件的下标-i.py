#
# @lc app=leetcode.cn id=2903 lang=python3
#
# [2903] 找出满足差值条件的下标 I
#
# @lc code=start
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        _max, _maxi = nums[0], 0
        _min, _mini = nums[0], 0
        
        left, right = 0, indexDifference
        n = len(nums)
        while left < n and right < n:
            if nums[left] > _max:
                _max = nums[left]
                _maxi = left
            if nums[left] < _min:
                _min = nums[left]
                _mini = left
            left += 1
            
            if abs(nums[right] - _max) >= valueDifference:
                return [_maxi, right]
            if abs(nums[right] - _min) >= valueDifference:
                return [_mini, right]
            right += 1
             
        return [-1, -1]
# @lc code=end


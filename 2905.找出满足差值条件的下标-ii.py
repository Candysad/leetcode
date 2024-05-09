#
# @lc app=leetcode.cn id=2905 lang=python3
#
# [2905] 找出满足差值条件的下标 II
#

# @lc code=start
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        '''
        双指针
        
        后面找一个符合距离的
        前面保留最大的和最小的
        '''
        n = len(nums)
        
        _min, _mini = nums[0], 0
        _max, _maxi = nums[0], 0
        last = 1
        now = indexDifference
        while now < n:
            if abs(nums[now] - _min) >= valueDifference:
                return [_mini, now]
            if abs(nums[now] - _max) >= valueDifference:
                return [_maxi, now]
            now += 1
            
            if last == n:
                break
            if _min > nums[last]:
                _min = nums[last]
                _mini = last
            if _max < nums[last]:
                _max = nums[last]
                _maxi = last
            last += 1
        return [-1, -1]
# @lc code=end


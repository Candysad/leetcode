#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        '''
        二分法直接维护窗口
        '''
        # window = sorted(nums[:k])
        # n = len(nums)
        # left = 0
        # right = k
        # result = []
        # median = lambda window: (window[(k-1)//2] + window[k//2]) / 2
        
        # result = [median(window)]
        # while right < n:
        #     window.remove(nums[left])
        #     window.insert(bisect_left(window, nums[right]), nums[right])
        #     result.append(median(window))
        #     left += 1
        #     right += 1
        # return result
        '''
        左右两个优先队列
        '''
        
        
# @lc code=end


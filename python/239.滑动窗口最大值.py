#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from heapq import *
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        for i in range(k):
            heappush(queue, (-nums[i], i))
        heapify(queue)
        
        left, right = 0, k
        result = [-queue[0][0]]
        
        n = len(nums)
        while right < n:
            heappush(queue, (-nums[right], right))
            
            while queue[0][1] <= left:
                heappop(queue)
            
            result.append(-queue[0][0])
            left += 1
            right += 1
        
        return result
# @lc code=end


#
# @lc app=leetcode.cn id=1671 lang=python3
#
# [1671] 得到山形数组的最少删除次数
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lefts = [1]
        queue = [nums[0]]
        for num in nums[1:]:
            if num > queue[-1]:
                queue.append(num)
                lefts.append(len(queue))
            else:
                i = bisect_left(queue, num)
                queue[i] = num
                lefts.append(i+1)
        
        rights = [1]
        queue = [nums[-1]]
        for num in nums[:-1][::-1]:
            if num > queue[-1]:
                queue.append(num)
                rights.append(len(queue))
            else:
                i = bisect_left(queue, num)
                queue[i] = num
                rights.append(i+1)
        
        n = len(nums)
        result = n - 1
        for i in range(1, n):
            if lefts[i] > 1 and rights[i] > 1:
                result = min(result, n - (lefts[i] + rights[i] - 1))
        return result  
# @lc code=end


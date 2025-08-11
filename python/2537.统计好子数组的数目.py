#
# @lc app=leetcode.cn id=2537 lang=python3
#
# [2537] 统计好子数组的数目
#
from collections import Counter
from math import comb
# @lc code=start
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, right, n = 0, 0, len(nums)
        counter = Counter()
        
        nows = 0
        result = 0
        while right < n:
            tr = counter[nums[right]]
            nows += tr
            counter[nums[right]] += 1
            right += 1
            
            while nows >= k:
                tl = counter[nums[left]]
                counter[nums[left]] -= 1
                nows -= tl - 1
                left += 1
            result += left
        
        return result    
# @lc code=end
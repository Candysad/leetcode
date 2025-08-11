#
# @lc app=leetcode.cn id=2598 lang=python3
#
# [2598] 执行操作后的最大 MEX
#
from collections import defaultdict,Counter
from math import inf
# @lc code=start
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        if value == 1:
            return len(nums)
        
        table = defaultdict(int)
        for num in nums:
            table[num % value] += 1
        
        result = inf
        for i in range(value):
            result = min(i + table[i] * value, result)
        return result
# @lc code=end
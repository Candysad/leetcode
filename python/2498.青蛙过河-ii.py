#
# @lc app=leetcode.cn id=2498 lang=python3
#
# [2498] 青蛙过河 II
#

# @lc code=start
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        if n < 4:
            return stones[-1] - stones[0]
        
        result = 0
        for i in range(2, n):
            result = max(result, stones[i] - stones[i-2])
        return result
# @lc code=end


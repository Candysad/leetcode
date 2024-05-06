#
# @lc app=leetcode.cn id=2568 lang=python3
#
# [2568] 最小无法得到的或值
#

# @lc code=start
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        for i in range(n):
            t = 1 << i
            if t not in nums:
                return t
        return 1 << n 
# @lc code=end


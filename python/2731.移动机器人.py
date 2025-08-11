#
# @lc app=leetcode.cn id=2731 lang=python3
#
# [2731] 移动机器人
#

# @lc code=start
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        for i in range(n):
            if s[i] == 'R':
                nums[i] += d
            else:
                nums[i] -= d
        nums.sort()
        
        result = 0
        presum = nums[0]
        for i in range(1, n):
            result += i * nums[i] - presum
            result %= mod
            presum += nums[i]
        
        return result
# @lc code=end
#
# @lc app=leetcode.cn id=2974 lang=python3
#
# [2974] 最小数字游戏
#
# @lc code=start
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        
        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i+1]
            result.append(b)
            result.append(a)
        
        return result
# @lc code=end
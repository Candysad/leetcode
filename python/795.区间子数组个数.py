#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        pre = -1 # 当前区间的左端点
        match = -1 # 当前区间的右端点
        result = 0
        for i, num in enumerate(nums):
            if num > right:
                pre = i
                match = -1
            elif num >= left:
                match = i
                result += match - pre
            else:
                if match != -1:
                    result += match - pre
        return result

# @lc code=end
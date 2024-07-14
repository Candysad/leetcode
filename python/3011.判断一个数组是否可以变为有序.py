#
# @lc app=leetcode.cn id=3011 lang=python3
#
# [3011] 判断一个数组是否可以变为有序
#

# @lc code=start
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        lastmax = 0
        lastbitcount = nums[0].bit_count()
        n = len(nums)
        
        now_min, now_max = nums[0], nums[0]
        
        i = 0
        while i < n:
            if nums[i].bit_count() != lastbitcount:
                if now_min < lastmax: return False
                else:
                    lastmax = now_max
                    now_min, now_max = nums[i], nums[i]
                    lastbitcount = nums[i].bit_count()
            else:
                now_min = min(now_min, nums[i])
                now_max = max(now_max, nums[i])
            
            i += 1
        if now_min < lastmax: return False
        return True
# @lc code=end
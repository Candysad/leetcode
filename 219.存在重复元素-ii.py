#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i, n in enumerate(nums):
            if n in table:
                if i - table[n] <= k:
                    return True
                else:
                    table[n] = i
            else:
                table[n] = i
        
        return False
# @lc code=end


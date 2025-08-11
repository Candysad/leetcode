#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#
from collections import defaultdict
# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        转成 198.打家劫舍
        两次O(n)遍历，时间复杂度O(n),
        '''
        table = defaultdict(int)
        
        for num in nums:
            table[num] += 1
        
        nums = sorted(list(table.keys()))
        last, dpb, dpt = -1, 0, 0
        for num in nums:
            b = max(dpb, dpt)
            if num != last + 1:
                t = max(dpt, dpb) + num * table[num]
            else:
                t = dpb + num * table[num]
            last = num
            dpb, dpt = b, t
        return max(dpb, dpt)
# @lc code=end


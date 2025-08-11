#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        异或
        初始为0，出现两次则异或回0
        单独的一个留下来
        '''
        result = 0
        for n in nums:
            result ^= n
        
        return result
# @lc code=end


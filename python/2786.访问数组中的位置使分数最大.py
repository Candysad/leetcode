#
# @lc app=leetcode.cn id=2786 lang=python3
#
# [2786] 访问数组中的位置使分数最大
#
from math import inf
# @lc code=start
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        '''
        反过来在最后一步确定 nums[0] 一定被选到
        '''
        # odd, even = 0, 0
        # for num in nums[::-1]:
        #     if num % 2:
        #         odd = max(odd, even - x) + num
        #     else:
        #         even = max(even, odd - x) + num
        
        # return odd if nums[0] % 2 else even
        
        '''
        正着选，保证第一次选和nums[0]奇偶不同的时候是从奇偶变过来的
        '''
        odd, even = -inf, -inf
        if nums[0] & 1:
            odd = nums[0]
        else:
            even = nums[0]
        
        for num in nums[1:]:
            if num & 1:
                odd = max(odd, even - x) + num
            else:
                even = max(even, odd - x) + num
        
        return max(odd, even)
# @lc code=end
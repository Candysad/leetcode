#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#
from functools import cache
# @lc code=start
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''
        两重逻辑的递归
        '''
        n = len(nums)
        _sum = sum(nums)
        
        @cache
        def dfs(left, right):
            if left > right:
                  return 0
            
            # 选左边
            t1 = nums[left] + min(dfs(left + 1, right-1), dfs(left+2, right))
            # 选右边
            t2 = nums[right] + min(dfs(left+1, right-1), dfs(left, right-2))
            return max(t1, t2)

        result = dfs(0, n-1)
        return result >= _sum - result
# @lc code=end


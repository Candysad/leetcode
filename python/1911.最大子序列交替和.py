#
# @lc app=leetcode.cn id=1911 lang=python3
#
# [1911] 最大子序列交替和
#
from math import inf
# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        preminus = 0 # 上一个刚减了一个数的
        preadd = nums[0] # 上一个刚加了一个数的
        
        for i, num in enumerate(nums):
            # 加上当前数
            nowadd = preminus + num
            # 直接减
            nowminus = preadd - num
            
            # 更新加了一个数的情况
            if nowadd > preadd:
                preadd = nowadd
            
            # 更新减了一个数的情况
            if nowminus > preminus:
                preminus = nowminus
        
        return max(preadd, preminus)
# @lc code=end
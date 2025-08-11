#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from collections import Counter
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        排序后从前往后遍历，留下最长的序列长度
        去重后再遍历效果差不多
        时间复杂度O(nlogn + n)，直接遍历代码还清晰一些
        '''
        # n = len(nums)
        # if n < 2:
        #     return n
        
        # nums.sort()
        # pivot = 1
        # now_result = 1
        # result = 1
        
        # while pivot < n:
        #     if nums[pivot] == nums[pivot-1] + 1:
        #         now_result += 1
        #     elif nums[pivot] != nums[pivot-1]:
        #         result = max(now_result, result)
        #         now_result = 1

        #     pivot += 1
        # result = max(now_result, result)
        # return result
        '''
        hash 表存数去重
        讲道理维护一个hash表时间并不是 O(n)
        '''
        nums = set(nums)
        result = 0
        
        for num in nums:
            if num - 1 not in nums:
                now = num # 一轮开始
                now_result = 1
                
                while now + 1 in nums:
                    now += 1
                    now_result += 1
                
                result = max(result, now_result)
        
        return result
                
        
        
# @lc code=end


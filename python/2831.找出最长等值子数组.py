#
# @lc app=leetcode.cn id=2831 lang=python3
#
# [2831] 找出最长等值子数组
#
from collections import defaultdict
# @lc code=start
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        '''
        滑动窗口
        '''
        n = len(nums)
        left, result = 0, 1
        counter = defaultdict(int)
        for right, n in enumerate(nums):
            counter[n] += 1
            while right-left+1 - counter[nums[left]] > k:
                counter[nums[left]] -= 1
                left += 1  
            result = max(result, counter[nums[right]])
        return result
                
        '''
        二分
        '''
        # # 存相同数字的下标
        # table = defaultdict(list)
        
        # result = 1
        # for i, n in enumerate(nums):
        #     if table[n]:
        #         tn = len(table[n])
        #         left, right = 0, tn-1
        #         while left <= right:
        #             mid = (left + right) >> 1
        #             # [table[n][mid], i)区间内字符个数 - 相同字符个数 
        #             c = (i - table[n][mid]) - (tn - mid)
        #             if c <= k:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
                
        #         result = max(result, tn - left + 1)
            
        #     table[n].append(i)
            
        # return result
# @lc code=end
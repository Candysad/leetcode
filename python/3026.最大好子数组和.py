#
# @lc app=leetcode.cn id=3026 lang=python3
#
# [3026] 最大好子数组和
#
from math import inf
from collections import defaultdict
from heapq import *
# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        从前向后遍历，记录前缀和
        每个数都做一个数组的末尾，就只需要找前面符合要求的最小的前缀和
        '''
        table = defaultdict(lambda: [inf, 0])
        pres = [0] * len(nums)
        pre = 0
        result = -inf
        for i, num in enumerate(nums):
            pre += num
            pres[i] = pre
            if pre < table[num][0]:
                table[num] = [pre, num]
            result = max(result, pre - table[num+k][0] + table[num+k][1])
            result = max(result, pre - table[num-k][0] + table[num-k][1])
        
        return result if result != -inf else 0
                    
        
        
# @lc code=end
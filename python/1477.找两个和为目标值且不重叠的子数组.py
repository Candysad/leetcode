#
# @lc app=leetcode.cn id=1477 lang=python3
#
# [1477] 找两个和为目标值且不重叠的子数组
#
from math import inf
from heapq import *
# @lc code=start
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        spans = []
        left, right = 0, 0
        _sum = 0
        n = len(arr)
        while right < n:
            if _sum < target:
                _sum += arr[right]
                right += 1
            
            elif _sum > target:
                _sum -= arr[left]
                left += 1
            
            if _sum == target:
                spans.append((left, right-1))
                _sum -= arr[left]
                left += 1
        while _sum > target:
            _sum -= arr[left]
            left += 1
            if _sum == target:
                spans.append((left, right-1))
                break
        
        stack = []
        result = inf
        for span in spans:
            ls = span[1] - span[0] + 1
            p = len(stack) - 1
            while p >= 0 and stack[p][1] >= span[0]:
                p -= 1
            
            if p >= 0:
                result = min(result, stack[p][0] + ls)
            
            if not stack or ls < stack[-1][0]:
                stack.append((ls, span[0], span[1]))
            
        return result if result != inf else -1

# @lc code=end


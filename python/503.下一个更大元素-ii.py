#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                prei, _ = stack.pop()
                result[prei] = num
            stack.append((i,num))
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                prei, _ = stack.pop()
                result[prei] = num
            stack.append((i,num))
        
        return result    
# @lc code=end
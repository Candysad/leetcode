#
# @lc app=leetcode.cn id=1673 lang=python3
#
# [1673] 找出最具竞争力的子序列
#

# @lc code=start
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i, num in enumerate(nums):
            least = max((k-(n-i), 0))
            while len(stack) > least and num < stack[-1]:
                stack.pop()
            stack.append(num)
    
        return stack[:k]
# @lc code=end


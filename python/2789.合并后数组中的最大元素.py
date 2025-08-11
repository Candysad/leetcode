#
# @lc app=leetcode.cn id=2789 lang=python3
#
# [2789] 合并后数组中的最大元素
#

# @lc code=start
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        '''
        贪心
        倒着遍历数组
        每一段满足的都从后往前加起来作为候选
        每一段加和中最大的作为答案
        考虑每一段边界和整体的边界
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # 找一段
        def find_a_span(right):
            # 找一段的最末
            while right >= 1 and nums[right] < nums[right-1]:
                right -= 1
            # 没找到，到开头了
            if right == 0:
                return nums[0], -1
            # 累加一段的和
            left = right - 1
            span_sum = nums[right]
            while left >= 0 and span_sum >= nums[left] :
                span_sum += nums[left]
                left -= 1
            return span_sum, left
        # 从后往前遍历
        result = 0
        right = n - 1
        while right > 0:
            t_sum, right = find_a_span(right)
            result = max(result, t_sum)
            
        # 单独判断开头
        if right == 0:
            result = max(result, nums[0])
        return result
# @lc code=end


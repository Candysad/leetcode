#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        
        left, right = 0, 1
        n = len(nums)
        result = []
        while right < n:
            if nums[right] == nums[right-1]+1:
                right += 1
            else:
                if left != right - 1:
                    result.append(str(nums[left]) + "->" + str(nums[right-1]))
                else:
                    result.append(str(nums[left]))
                left = right
                right += 1
        if left != n-1:
            result.append(str(nums[left]) + "->" + str(nums[n-1]))
        else:
            result.append(str(nums[n-1]))  
        return result
# @lc code=end
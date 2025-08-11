#
# @lc app=leetcode.cn id=2934 lang=python3
#
# [2934] 最大化数组末位元素的最少操作次数
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        max1, max2 = nums1[-1], nums2[-1]
        result = 0
        both = 0
        for i in range(n-1):
            num1, num2 = nums1[i], nums2[i]
            num11, num12 = num1 <= max1, num1 <= max2
            num21, num22 = num2 <= max1, num2 <= max2
            
            if num11 and num12 and num21 and num22: # 完全不用交换，随便放
                both += 1 
            
            if num11 and num22: continue # 不用换
            else:
                if num21 and num12: result += 1 # 需要换且能换
                else: return -1 # 需要换但是换不得
        
        return min(result, n-result-both) # 翻转后再去除完全不用交换的位置
# @lc code=end


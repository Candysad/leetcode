#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        t = sorted(nums)
        i, j, k = 0, (n-1) // 2, n-1
        while i < n:
            nums[i] = t[j]
            if i + 1 < n:
                nums[i+1] = t[k]
            
            i += 2
            j -= 1
            k -= 1
# @lc code=end


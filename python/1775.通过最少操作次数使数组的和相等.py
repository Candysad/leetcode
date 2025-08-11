#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2: return 0
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            nums1, nums2 = nums2, nums1
        target = sum2 - sum1
        nums1.sort(reverse=True)
        nums2.sort()
        p1, p2 = len(nums1)-1, len(nums2)-1
        
        result = 0
        while target > 0 and (p1 >= 0 or p2 >= 0):
            n1 = 6 - nums1[p1] if p1 >= 0 else -1
            n2 = nums2[p2] - 1 if p2 >= 0 else -1
            
            if n1 > n2:
                target -= n1
                p1 -= 1
            else:
                target -= n2
                p2 -= 1
            result += 1

        if target > 0: return -1
        return result
# @lc code=end
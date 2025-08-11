#
# @lc app=leetcode.cn id=3002 lang=python3
#
# [3002] 移除后集合的最多元素数
#

# @lc code=start
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        sc = s1.intersection(s2)
        
        n = len(nums1)
        target = n // 2
        l1, l2 = len(s1), len(s2)
        r1, r2 = max(target - n + l1, 0) , max(target - n + l2, 0)
        rc = len(sc)
        
        if r1 >= rc:
            r1 -= rc
            l1 -= rc
            rc = 0
        elif rc > r1:
            rc -= r1
            l1 -= r1
            r1 = 0
        
        if r2 >= rc:
            r2 -= rc
            l2 -= rc
            rc = 0
        elif rc > r2:
            rc -= r2
            l2 -= r2
            r2 = 0
        
        l1 -= r1
        l2 -= r2
        return l1 + l2 - rc    
# @lc code=end
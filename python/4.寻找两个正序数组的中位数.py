#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from heapq import *
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        flag = (m + n) % 2 == 0
        
        def findk(k):
            p1, p2 = 0, 0
            
            while True:
                if p1 == m:
                    return nums2[p2 + k - 1]
                if p2 == n:
                    return nums1[p1 + k - 1]
                if k == 1:
                    return min(nums1[p1], nums2[p2])
                
                t1 = min(p1 + k//2 - 1, m-1)
                t2 = min(p2 + k//2 - 1, n-1)
                
                if nums1[t1] < nums2[t2]:
                    k -= t1 - p1 + 1
                    p1 = t1 + 1
                else:
                    k -= t2 - p2 + 1
                    p2 = t2 + 1
        
        if flag:
            return (findk((m+n) // 2) + findk((m+n-1)//2)) / 2

        return findk((m+n) // 2 + 1)
# @lc code=end
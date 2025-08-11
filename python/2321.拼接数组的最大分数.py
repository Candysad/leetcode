#
# @lc app=leetcode.cn id=2321 lang=python3
#
# [2321] 拼接数组的最大分数
#

# @lc code=start
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        动态规划
        对于nums1 
        dp1[i] 第一段里选 dp2[i] 不选 dp3[i] 第二段里选
        '''
        n = len(nums1)
        dp11, dp12, dp13 = 0, 0, 0
        dp21, dp22, dp23 = 0, 0, 0
        for i in range(n):
            t1, t2, t3 = dp11, dp12, dp13
            dp11 = t1 + nums1[i]
            dp12 = max(t1, t2) + nums2[i]
            dp13 = max(t2, t3) + nums1[i]
            
            t1, t2, t3 = dp21, dp22, dp23
            dp21 = t1 + nums2[i]
            dp22 = max(t1, t2) + nums1[i]
            dp23 = max(t2, t3) + nums2[i]

        return max(dp11, dp12, dp13, dp21, dp22, dp23)
# @lc code=end


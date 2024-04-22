#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 数字范围 -10000~10000
        linkhash = [0] * 20001
        for n in nums:
            linkhash[n+10000] += 1
        
        for i in range(20000, -1, -1):
            k -= linkhash[i]
            if k <= 0:
                return i-10000
        
# @lc code=end


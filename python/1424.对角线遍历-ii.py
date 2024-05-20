#
# @lc app=leetcode.cn id=1424 lang=python3
#
# [1424] 对角线遍历 II
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        ns = []
        for line in nums:
            ns.append(len(line))
        n = max(ns) + 1
        result = []
        
        # 从上到下
        for i in range(m):
            x, y = i, 0
            while x >= 0 and y < n:
                if y < ns[x]:
                    result.append(nums[x][y])

                x -= 1
                y += 1
        
        # 从左到右
        for i in range(n):
            x, y = m-1, i
            while x >= 0 and y < n:
                if y < ns[x]:
                    result.append(nums[x][y])

                x -= 1
                y += 1
        
        return result
        
# @lc code=end


#
# @lc app=leetcode.cn id=1424 lang=python3
#
# [1424] 对角线遍历 II
#
from collections import deque
# @lc code=start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        ns = []
        for line in nums:
            ns.append(len(line))
        
        queue = deque()
        result = []
        
        # 贴着左边从上到下
        for i in range(m):
            queue.appendleft((i, 0))
            
            t = queue
            queue = deque()
            for x, y in t:
                result.append(nums[x][y])
                if y + 1 < ns[x]:
                    queue.append((x, y+1))
        
        # 贴着下面从左到右
        while queue:
            t = queue
            queue = deque()
            for x, y in t:
                result.append(nums[x][y])
                if y + 1 < ns[x]:
                    queue.append((x, y+1))
        
        return result    
# @lc code=end


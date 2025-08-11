#
# @lc app=leetcode.cn id=2684 lang=python3
#
# [2684] 矩阵中移动的最大次数
#

# @lc code=start
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        '''
        依次比较总会有重复
        用max min确定边界
        '''
        m = len(grid)
        n = len(grid[0])
        if n == 1:
            return 0
         
        # 初始第一列 
        result = 0
        queue = {i:0 for i in range(m)} # queue装左列可用格子，也起左指针作用
        while result < n - 1:
            t = queue
            queue = {}
            for left in t.keys():
                for right in range(max(0, left-1), min(m, left+2)):
                    if grid[left][result] < grid[right][result+1]:
                        queue[right] = 0
            if queue:
                result += 1
            else:
                break
        return result
  
# @lc code=end


#
# @lc app=leetcode.cn id=1536 lang=python3
#
# [1536] 排布二进制网格的最少交换次数
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def check(line):
            for j in range(n-1, -1, -1):
                if line[j] == 1: break
            
            if j != 0: return n-1-j
            elif line[0] == 0: return n
            return n-1
            
        queue = []
        for i, line in enumerate(grid):
            queue.append((i, check(line)))
        
        now = n-1
        tq = queue.copy()
        tq.sort(key=lambda x: x[1])
        for _, num in tq[::-1]:
            if num >= now:
                now -= 1
            else: return -1
            
        result = 0
        for i in range(n):
            target = n - 1 - i
            for j in range(i, n):
                if queue[j][1] <= target:
                    result += j - i
                else: break
                
            for k in range(j, i, -1):
                queue[k], queue[k-1] = queue[k-1], queue[k]
                
        return result
# @lc code=end
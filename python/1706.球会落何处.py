#
# @lc app=leetcode.cn id=1706 lang=python3
#
# [1706] 球会落何处
#

# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        balls = [j for j in range(n)]
        
        for i in range(m):
            for j in range(n):
                index = balls[j]
                if index == -1: continue
                
                elif index == 0 and grid[i][index] == -1:
                        balls[j] = -1
                elif index == n-1 and grid[i][index] == 1:
                    balls[j] = -1
                        
                elif grid[i][index] == 1 and grid[i][index+1] == 1:
                    balls[j] += 1
                elif grid[i][index] == -1 and grid[i][index-1] == -1:
                    balls[j] -= 1
                else:
                    balls[j] = -1
           
        return balls
# @lc code=end


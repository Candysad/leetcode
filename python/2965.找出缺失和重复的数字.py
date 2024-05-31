#
# @lc app=leetcode.cn id=2965 lang=python3
#
# [2965] 找出缺失和重复的数字
#

# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a, _sum = 0, 0
        for i in range(n):
            for j in range(n):
                num = abs(grid[i][j])
                _sum += num
                num -= 1
                
                x = num // n
                y = num % n
                if grid[x][y] < 0:
                    a = num + 1
                else:
                    grid[x][y] *= -1

        b = (1+n*n)*n*n // 2 - _sum + a
        return [a, b]
# @lc code=end


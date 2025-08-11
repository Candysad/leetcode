#
# @lc app=leetcode.cn id=3030 lang=python3
#
# [3030] 找出网格的区域平均强度
#
from math import floor
# @lc code=start
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        result = [[[0, 0] for _ in range(n)] for __ in range(m)]
        
        def isblock(i, j):
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if x + 1 < i + 3 and abs(image[x+1][y] - image[x][y]) > threshold:
                        return False

                    if y + 1 < j + 3 and abs(image[x][y+1] - image[x][y]) > threshold:
                        return False
            
            return True
        
        def blcoksum(i, j):
            _sum = 0
            for x in range(i, i+3):
                _sum += sum(image[x][j:j+3])
            
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if result[x][y][1] == 0:
                        result[x][y][0] = _sum / 9
                    elif result[x][y][1] == 1:
                        result[x][y][0] = floor(result[x][y][0])
                        result[x][y][0] += floor(_sum / 9)
                    else:
                        result[x][y][0] += floor(_sum / 9)
                    
                    result[x][y][1] += 1
        
        for i in range(m-2):
            for j in range(n-2):
                if isblock(i, j):
                    blcoksum(i, j)
        
        for i in range(m):
            for j in range(n):
                if result[i][j][1]:
                    result[i][j] = floor(result[i][j][0] / result[i][j][1])
                else:
                    result[i][j] = image[i][j]
        
        return result
# @lc code=end
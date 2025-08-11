#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        bound = [m-1, 0, n-1, 1] # right, left, down, up
        result = []
        total = n * m
        
        def go(direct: str, index, bound):
            right, left, down, up = bound
            i, j = index
            
            
            if direct == 'r':
                while j < right:
                    result.append(matrix[i][j])
                    j += 1
                right -= 1
            elif direct == 'd':
                while i < down:
                    result.append(matrix[i][j])
                    i += 1
                down -= 1
            elif direct == 'l':
                while j > left:
                    result.append(matrix[i][j])
                    j -= 1
                left += 1
            elif direct == 'u':
                while i > up:
                    result.append(matrix[i][j])
                    i -= 1
                up += 1
            
            
            if len(result) == total - 1:
                result.append(matrix[i][j])
                return False
            
            index[:] = [i, j]
            bound[:] = [right, left, down, up]
            return True
        
        
        direction  = {
            0: 'r',
            1: 'd',
            2: 'l',
            3: 'u'
        }
        direct = 0
        index = [0, 0]
        while go(direction[direct], index, bound):
            direct = (direct + 1) % 4
        
        return result

# @lc code=end


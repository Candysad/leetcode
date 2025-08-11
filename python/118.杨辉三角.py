#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        '''
        cheat table
        '''
        self.result = [[1]]
        queue = [1]   
        for i in range(2, 31):
            t = queue
            queue = [1]
            for right in range(1, len(t)):
                queue.append(t[right-1] + t[right])
            queue.append(1)
            self.result.append(queue)
    
    def generate(self, numRows: int) -> List[List[int]]:
        return self.result[ : numRows]
        
        '''
        正推
        '''
        result = [[1]]
        if numRows == 1:
            return result
        
        queue = [1]
        
        for i in range(2, numRows+1):
            t = queue
            queue = [1]
            for right in range(1, len(t)):
                queue.append(t[right-1] + t[right])
            queue.append(1)
            result.append(queue)
        
        return result
# @lc code=end


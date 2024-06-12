#
# @lc app=leetcode.cn id=1504 lang=python3
#
# [1504] 统计全 1 子矩形
#

# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        '''
        单调栈记录上面每横最左到多左，取最少的那个
        '''
        m = len(mat)
        n = len(mat[0])
        stacks = [[] for _ in range(n)]        
        for i in range(m):
            pre = 0
            for j in range(n):
                if mat[i][j] == 1:
                    pre += 1
                    stacks[i][j] = pre
        
        result = 0
        
        
        return result
        
        
        '''
        方向反了变成暴力了
        '''
        m = len(mat)
        n = len(mat[0])
        stacks = [0] * n
        result = 0
        
        for i in range(m):
            pre = 0
            for j in range(n):
                if mat[i][j] == 1:
                    pre += 1
                    for k in range(j, j-pre, -1):
                        t = max(stacks[k : j+1])
                        result += i - t + 1
                else:
                    stacks[j] = i + 1
        return result
# @lc code=end
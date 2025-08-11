#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        从 (0, 0) 起到达 (m-1, n-1)
        向下m-1次，向右n-1次，共m+n-2次动作
        其中选择m-1个动作为向下，其余自动为向右
        即 $C^{m-1}_{m+n-2} = \frac{(m+n-2)!}{(n-1)! (m-1)! }
        '''
        # return comb(m+n-2, m-1)
    
        '''
        动态规划
        除边界外每个格子都来自于上或下两种情况
        
        原地单数组，降低空间复杂度
        '''
        f = [1] * n
        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    f[j] = f[j]
                else:
                    f[j] = f[j-1] + f[j]
        
        return f[-1]
# @lc code=end
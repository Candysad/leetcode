#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s) # 长度
        n = len(p)
        
        def check(i, j):
            # 外面下标从1开始算的
            if i == 0:       # 目标已经到头，不管模式还有没有都不用比了，就算模式里有 * 也不需要这里判断
                return False
            
            if p[j-1] == '.':  # "."一定匹配
                return True
            
            # 字符相同
            return s[i - 1] == p[j - 1]
        
        # 状态矩阵
        f = [[False] * (n + 1) for _ in range(m + 1)] # 额外设置了起始，所以size + 1
        f[0][0] = True # 起始设置为 True，能匹配到起始则成功
        
        for i in range(m+1):
            for j in range(1, n+1): 
                if p[j-1] == '*':
                    f[i][j] |= f[i][j - 2] #零次匹配，或者不匹配
                    if check(i, j - 1): # 匹配一次
                        f[i][j] |= f[i - 1][j] # 目标前挪，模式留在 "*"继续等待匹配
                else:
                    if check(i, j): # 字符相同
                        f[i][j] |= f[i - 1][j - 1]
        # 返回矩阵右下角的位置
        return f[m][n]  
# @lc code=end
#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        '''
        递归
        '''
        nums = set([str(i) for i in range(10)])
        
        def anum(i):# 从i起向后找一个数字，返回这个数字和下一个[之后的坐标
            t = []
            while s[i] != '[':
                t.append(s[i])
                i += 1
            return int(''.join(t).lstrip('0')), i + 1 # 返回数字后[]内部的起始位置
        
        def astr(i):# 从i起向后找一个普通字符串,返回这个字符串和它结束后的下一个坐标（可能是数字或]）
            t = []
            while s[i] !=']' and s[i] not in nums:
                t.append(s[i])
                i += 1
            return ''.join(t), i # 最后一个位置不再是字母，是数字或则达到边界
                
        def dfs(i): # 返回一个括号内的区域形成的字符串和区域]之后的坐标
            t = []
            # 到达整体的结尾或者当前层的 ]
            while i < len(s) and s[i] != ']':
                if s[i] not in nums: # 不是数字是普通字符串
                  ts, i = astr(i)
                  t.append(ts)
                
                if s[i] in nums:# 发现数字
                    tn, i = anum(i)# 得到数字和后续[]内的起始位置
                    ts, i = dfs(i) # 递归进去得到里面的字符串，并得到下一个坐标
                    t.append(tn * ts)
            
            # 返回当前层的字符串和下一个坐标
            return ''.join(t), i+1
        
        s = '1[' + s + ']'
        result, _ = dfs(0)
        return result
 
# @lc code=end


#
# @lc app=leetcode.cn id=2351 lang=python3
#
# [2351] 第一个出现两次的字母
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        '''
        简单题
        一次遍历同时存前面信息
        '''
        t_dic = {}
        for c in s:
            if t_dic.get(c,0):
                return c
            else:
                t_dic[c] = 1
            
# @lc code=end


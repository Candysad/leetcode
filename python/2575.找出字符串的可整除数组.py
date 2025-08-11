#
# @lc app=leetcode.cn id=2575 lang=python3
#
# [2575] 找出字符串的可整除数组
#

# @lc code=start
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        '''
        取余的数学题
        直接保留每次的数字会太大
        
        十倍a取余等于十个a分别取余再求和（乘十），最后再取一次余
        相当于上一次取余的结果(a mode m)，变成十倍，再和新的b相加
        所以每次保留上次取余的结果，翻十倍再加上新的个位之后取余就是新的数取余的结果
        '''
        result = []
        now = 0
        for c in word:
            now = (now * 10 + int(c)) % m
            result.append(0 if now else 1)
        return result         
# @lc code=end


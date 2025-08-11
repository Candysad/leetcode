#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        数据结构题
        逆序添加逆序输出
        分别处理下标越界
        '''
        result = []
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            t = n1 + n2 + carry
            result.append(str(t % 10))
            carry = t // 10
            i -= 1
            j -= 1 
        return ''.join(result[::-1])      
# @lc code=end
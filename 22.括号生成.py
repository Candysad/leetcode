#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        递归
        加入左括号的情况和加入右括号的情况分别讨论
        '''
        result = []
        def gen(s: str, left:int, right:int):
            if left == 0 and right == 0:
                result.append(s)
            
            # 加入一个左括号
            # 可放入的左括号数量-1，可放入的右括号数量+1
            if left:
                gen(s+"(", left-1, right+1)
            # 
            if right:
                gen(s+")", left, right-1)
        
        gen("", n, 0)
        return result
# @lc code=end


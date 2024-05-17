#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        递归+回溯
        加入左括号的情况和加入右括号的情况分别讨论
        '''
        result = []
        pre = []
        def dfs(left:int, right:int) -> None:
            if left == right == n:
                result.append(''.join(pre))
                return
            
            if left < n:
                pre.append('(')
                dfs(left+1, right)
                pre.pop()
            
            if left > right:
                pre.append(")")
                dfs(left, right+1)
                pre.pop()
            
        dfs(0, 0)
            
        return result
# @lc code=end


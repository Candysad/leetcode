#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        
        def dfs(left, right):
            if left == n and right == n:
                result.append(''.join(path))
                return
            
            if right < left:
                path.append(')')
                dfs(left, right+1)
                path.pop()
            
            if left < n:
                path.append('(')
                dfs(left+1, right)
                path.pop()
        
        dfs(0, 0)
        return result
# @lc code=end


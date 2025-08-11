#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        wn = len(word)
        
        pre = set()
        def dfs(i, j, ci):
            if ci == wn:
                return True
            if 0 <= i < n and 0 <= j < m:
                if (i, j) not in pre and board[i][j] == word[ci]:
                    pre.add((i, j))
                    result = False
                    for nexti, nextj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                        result |= dfs(nexti, nextj, ci+1)
                    pre.remove((i, j))
                    return result
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False  
# @lc code=end


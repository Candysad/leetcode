#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        
        tree = {"end": False}
        def add(word):
            now = tree
            for c in word:
                next = now.get(c, {"end": False})
                now[c] = next
                now = next
            now['end'] = True
        for word in words:
            add(word)
        
        
        result = set()
        path = []
        vis = set()
        now = tree
        def dfs(i, j):
            nonlocal now
            if now['end']:
                result.add(''.join(path))
            
            c = board[i][j]
            next = now.get(c, None)
            if next is None: return
            pre = now
            now = next
            vis.add((i, j))
            
            path.append(c)
            for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in vis:
                        dfs(x, y)
            
            path.pop()
            vis.remove((i, j))
            now = pre
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return list(result)
# @lc code=end